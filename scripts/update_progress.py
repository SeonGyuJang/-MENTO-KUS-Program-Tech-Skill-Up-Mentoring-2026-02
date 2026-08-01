"""
T-SUM Mentor Progress Auto-Updater
------------------------------------
unit-1 ~ unit-8 폴더의 아래 두 항목을 체크합니다.
  1. 실습 파일 : .ipynb 또는 .py 존재 여부
  2. 노션 정리본 : notion.txt 존재 여부
"""

import os
import re
from datetime import datetime, timezone, timedelta

UNITS = {
    "unit-1": {"title": "Intro to Deep RL"},
    "unit-2": {"title": "Q-Learning"},
    "unit-3": {"title": "Deep Q-Learning (DQN)"},
    "unit-4": {"title": "Policy Gradient (REINFORCE)"},
    "unit-5": {"title": "Unity ML-Agents"},
    "unit-6": {"title": "Actor-Critic (A2C)"},
    "unit-7": {"title": "Multi-Agent RL (MARL)"},
    "unit-8": {"title": "PPO"},
}

PRACTICE_EXTS = {".ipynb", ".py"}
NOTION_FILE   = "notion.txt"
README_PATH   = "README.md"
KST           = timezone(timedelta(hours=9))

def check_unit(folder: str):
    """(has_practice, has_notion) 반환"""
    if not os.path.isdir(folder):
        return False, False
    files = os.listdir(folder)
    has_practice = any(
        os.path.splitext(f)[1].lower() in PRACTICE_EXTS for f in files
    )
    has_notion = NOTION_FILE in files
    return has_practice, has_notion

statuses  = {k: check_unit(k) for k in UNITS}
completed = sum(1 for p, n in statuses.values() if p or n)
total     = len(UNITS)
pct       = int(completed / total * 100)

BAR_LEN = 20
filled  = round(pct / 100 * BAR_LEN)
bar     = "█" * filled + "░" * (BAR_LEN - filled)

rows = []
for folder, info in UNITS.items():
    has_p, has_n = statuses[folder]
    icon      = "✅" if (has_p and has_n) else ("🔶" if (has_p or has_n) else "⬜")
    p_str     = "✅" if has_p else "❌"
    n_str     = "✅" if has_n else "❌"
    unit_num  = folder.replace("unit-", "")
    rows.append(
        f"| {icon} | **Unit {unit_num}** | {info['title']} | {p_str} | {n_str} |"
    )

table   = "\n".join(rows)
now_kst = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

progress_block = f"""<!-- PROGRESS_START -->
## 📋 수업 진행 현황

<div align="center">

### `{bar}` &nbsp; {completed} / {total} Units &nbsp; **{pct}%**

🕐 마지막 업데이트: {now_kst}

<br>

| 상태 | Unit | 주제 | 실습 파일 | 노션 정리본 |
|:---:|:---:|:---:|:---:|:---:|
{table}

</div>

> 📌 각 Unit 폴더에 실습 파일(`.ipynb`/`.py`)과 노션 링크(`notion.txt`)를 업로드하면 진행도가 자동으로 갱신됩니다.

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
