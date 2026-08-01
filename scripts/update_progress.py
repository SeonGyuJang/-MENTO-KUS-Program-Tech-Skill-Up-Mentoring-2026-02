"""
T-SUM Mentor Progress Auto-Updater
------------------------------------
unit-1 ~ unit-8 폴더에 note.md 또는 curriculum.md 파일이 존재하는지 확인하고
README.md 의 <!-- PROGRESS_START --> ~ <!-- PROGRESS_END --> 블록을 자동 갱신합니다.
"""

import os
import re
from datetime import datetime, timezone, timedelta

UNITS = {
    "unit-1": {"title": "Intro to Deep RL",            "env": "LunarLander"},
    "unit-2": {"title": "Q-Learning",                  "env": "FrozenLake / Taxi"},
    "unit-3": {"title": "Deep Q-Learning (DQN)",       "env": "Space Invaders"},
    "unit-4": {"title": "Policy Gradient (REINFORCE)",  "env": "CartPole / Pixelcopter"},
    "unit-5": {"title": "Unity ML-Agents",             "env": "SnowballTarget / Pyramids"},
    "unit-6": {"title": "Actor-Critic (A2C)",          "env": "PyBullet Robotics"},
    "unit-7": {"title": "Multi-Agent RL (MARL)",       "env": "Soccer 2v2"},
    "unit-8": {"title": "PPO",                         "env": "LunarLander / VizDoom"},
}

NOTE_FILE       = "note.md"
CURRICULUM_FILE = "curriculum.md"
README_PATH     = "README.md"
KST             = timezone(timedelta(hours=9))

def check_folder(folder: str):
    """note.md, curriculum.md 존재 여부를 (bool, bool) 로 반환"""
    if not os.path.isdir(folder):
        return False, False
    files = os.listdir(folder)
    has_note = NOTE_FILE in files
    has_curr = CURRICULUM_FILE in files
    return has_note, has_curr

statuses  = {k: check_folder(k) for k in UNITS}
completed = sum(1 for n, cu in statuses.values() if n or cu)
total     = len(UNITS)
pct       = int(completed / total * 100)

BAR_LEN = 20
filled  = round(pct / 100 * BAR_LEN)
bar     = "█" * filled + "░" * (BAR_LEN - filled)

rows = []
for folder, info in UNITS.items():
    has_note, has_curr = statuses[folder]
    icon      = "✅" if (has_note or has_curr) else "⬜"
    note_str  = "업로드" if has_note else "미업로드"
    curr_str  = "업로드" if has_curr else "미업로드"
    unit_num  = folder.replace("unit-", "")
    rows.append(
        f"| {icon} | **Unit {unit_num}** | {info['title']} | {note_str} | {curr_str} |"
    )

table   = "\n".join(rows)
now_kst = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

progress_block = f"""<!-- PROGRESS_START -->
## 📋 수업 진행 현황

<div align="center">

### `{bar}` &nbsp; {completed} / {total} Units &nbsp; **{pct}%**

🕐 마지막 업데이트: {now_kst}

<br>

| 상태 | Unit | 주제 | 정리본 | 커리큘럼 메모 |
|:---:|:---:|:---:|:---:|:---:|
{table}

</div>

> 📌 각 Unit 폴더에 파일을 업로드하면 진행도가 자동으로 갱신됩니다.

---
<!-- PROGRESS_END -->"""

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"<!-- PROGRESS_START -->.*?<!-- PROGRESS_END -->"
if re.search(pattern, content, flags=re.DOTALL):
    new_content = re.sub(pattern, progress_block, content, flags=re.DOTALL)
else:
    new_content = content.replace("\n---\n", f"\n{progress_block}\n---\n", 1)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Mentor progress updated: {completed}/{total} ({pct}%)")
