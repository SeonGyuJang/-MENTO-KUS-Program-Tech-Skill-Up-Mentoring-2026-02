"""
╔══════════════════════════════════════════════════════════════════╗
║      T-SUM Deep RL — 멘토 레포지토리 자동 생성 스크립트             ║
║    실행하면 현재 디렉토리에 멘토용 폴더 구조가 바로 생성됩니다          ║
╚══════════════════════════════════════════════════════════════════╝

사용법:
    python setup_tsum_mentor_repo.py

Python 3.8 이상, 외부 라이브러리 불필요 (표준 라이브러리만 사용)
"""

import os
import sys
import textwrap

# ══════════════════════════════════════════════════════════════════════════════
# 0. 색상 출력 헬퍼
# ══════════════════════════════════════════════════════════════════════════════

def c(text, code):
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7
            )
        except Exception:
            return text
    return f"\033[{code}m{text}\033[0m"

def info(msg):  print(c(f"  ✔  {msg}", "32"))
def warn(msg):  print(c(f"  ⚠  {msg}", "33"))
def head(msg):  print(c(f"\n{'━'*60}\n  {msg}\n{'━'*60}", "36"))
def done(msg):  print(c(f"\n  🎉 {msg}", "35"))

# ══════════════════════════════════════════════════════════════════════════════
# 1. 파일 내용 정의
# ══════════════════════════════════════════════════════════════════════════════

README_CONTENT = """\
<div align="center">

<img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="55px"/>

# T-SUM · Deep Reinforcement Learning

**Tech Skill Up Mentoring — 멘토 자료 레포지토리**

고려대학교 세종캠퍼스 학생복지처 취창업지원센터

</div>

---

<!-- PROGRESS_START -->
## 📋 수업 진행 현황

<div align="center">

### `░░░░░░░░░░░░░░░░░░░░` &nbsp; 0 / 8 Units &nbsp; **0%**

🕐 마지막 업데이트: -

<br>

| 상태 | Unit | 주제 | 정리본 | 커리큘럼 메모 |
|:---:|:---:|:---:|:---:|:---:|
| ⬜ | **Unit 1** | Intro to Deep RL | 미업로드 | 미업로드 |
| ⬜ | **Unit 2** | Q-Learning | 미업로드 | 미업로드 |
| ⬜ | **Unit 3** | Deep Q-Learning (DQN) | 미업로드 | 미업로드 |
| ⬜ | **Unit 4** | Policy Gradient (REINFORCE) | 미업로드 | 미업로드 |
| ⬜ | **Unit 5** | Unity ML-Agents | 미업로드 | 미업로드 |
| ⬜ | **Unit 6** | Actor-Critic (A2C) | 미업로드 | 미업로드 |
| ⬜ | **Unit 7** | Multi-Agent RL (MARL) | 미업로드 | 미업로드 |
| ⬜ | **Unit 8** | PPO | 미업로드 | 미업로드 |

</div>

> 📌 각 Unit 폴더에 파일을 업로드하면 진행도가 자동으로 갱신됩니다.

---
<!-- PROGRESS_END -->

## 📌 레포지토리 소개

본 레포지토리는 **고려대학교 세종캠퍼스 학생복지처 취창업지원센터**가 주관하는 **T-SUM(Tech Skill Up Mentoring) 프로그램**의 **멘토 자료 저장소**입니다.

[HuggingFace Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)를 기반으로 Unit 1~8의 **개념 정리본, 수업 계획 메모**를 체계적으로 관리하며, 멘티들의 학습을 지원하기 위한 참고 자료를 공개합니다.

---

## 🗂️ 레포지토리 구조

```
📦 T-SUM-Deep-RL-Course-Mentor
│
├── 📁 .github/
│   └── 📁 workflows/
│       └── ⚙️  update-progress.yml     # 진행도 자동 업데이트 Action
│
├── 📁 scripts/
│   └── 🐍 update_progress.py          # 진행도 계산 스크립트
│
├── 📁 unit-1/                         # Introduction to Deep RL
│   ├── 📄 note.md                     # 개념 정리본
│   └── 📄 curriculum.md               # 수업 진행 계획 메모
├── 📁 unit-2/                         # Q-Learning
├── 📁 unit-3/                         # Deep Q-Learning (DQN)
├── 📁 unit-4/                         # Policy Gradient
├── 📁 unit-5/                         # Unity ML-Agents
├── 📁 unit-6/                         # Actor-Critic (A2C)
├── 📁 unit-7/                         # Multi-Agent RL
├── 📁 unit-8/                         # PPO (Part 1 & 2)
│
└── 📄 README.md
```

> 각 `unit-N/` 폴더에 `note.md` 또는 `curriculum.md` 파일이 업로드되면 GitHub Actions가 자동으로 진행도를 갱신합니다.

---

## 📚 커리큘럼

### Unit 1 — Introduction to Deep Reinforcement Learning

> 강화학습의 기초 개념과 첫 번째 에이전트 구현

강화학습(RL)의 전반적인 학습 프레임워크를 이해하고, 에이전트(Agent)·환경(Environment)·보상(Reward)·정책(Policy) 등 핵심 개념을 학습합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | RL Framework, MDP, Agent-Environment Interaction |
| 실습 환경 | `LunarLander-v2` |
| 주요 라이브러리 | `stable-baselines3`, `gymnasium` |
| 멘토 자료 경로 | `unit-1/` |

</div>

---

### Unit 2 — Introduction to Q-Learning

> 가치 기반 학습의 핵심: Q-테이블 직접 구현

Markov Decision Process(MDP)와 벨만 방정식(Bellman Equation)을 이해하고, Q-Learning 에이전트를 처음부터(scratch) 구현합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Q-Table, Bellman Equation, ε-Greedy Policy, TD Learning |
| 실습 환경 | `FrozenLake-v1`, `Taxi-v3` |
| 주요 라이브러리 | `numpy`, `gymnasium` |
| 멘토 자료 경로 | `unit-2/` |

</div>

---

### Unit 3 — Deep Q-Learning with Atari Games

> 신경망을 결합한 DQN으로 Atari 게임 정복

Q-Learning의 한계와 Deep Q-Network(DQN)의 핵심 안정화 기법(Experience Replay, Fixed Q-Target)을 이해합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | DQN, Experience Replay, Fixed Q-Target, CNN |
| 실습 환경 | `SpaceInvadersNoFrameskip-v4` |
| 주요 라이브러리 | `rl-baselines3-zoo`, `gymnasium[atari]` |
| 멘토 자료 경로 | `unit-3/` |

</div>

---

### Unit 4 — Policy Gradient with PyTorch

> 정책 직접 최적화: REINFORCE 알고리즘 구현

Policy-Based 방법론의 이론을 학습하고, PyTorch로 REINFORCE 알고리즘을 직접 구현합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Policy Gradient, REINFORCE, Stochastic Policy |
| 실습 환경 | `CartPole-v1`, `Pixelcopter-PLE-v0` |
| 주요 라이브러리 | `torch`, `gymnasium` |
| 멘토 자료 경로 | `unit-4/` |

</div>

---

### Unit 5 — Introduction to Unity ML-Agents

> Unity 게임 엔진 기반 강화학습 환경 실습

Unity ML-Agents 툴킷의 구조와 활용법을 이해하고, 3D 시뮬레이션 환경에서 에이전트를 학습시킵니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | ML-Agents Toolkit, Unity Environment |
| 실습 환경 | `SnowballTarget`, `Pyramids` |
| 주요 라이브러리 | `mlagents` |
| 멘토 자료 경로 | `unit-5/` |

</div>

---

### Unit 6 — Actor-Critic Methods with Robotics

> 가치 기반 + 정책 기반의 결합: A2C 알고리즘

Actor-Critic 아키텍처와 Advantage Function을 이해하고, 로봇 제어 환경에 적용합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Actor-Critic, A2C, Advantage Function, Continuous Action Space |
| 실습 환경 | `PyBullet` Robotics Environments |
| 주요 라이브러리 | `stable-baselines3`, `pybullet` |
| 멘토 자료 경로 | `unit-6/` |

</div>

---

### Unit 7 — Multi-Agent Reinforcement Learning

> 다수의 에이전트가 협력·경쟁하는 MARL

MARL의 핵심 개념과 Self-Play 전략을 이해하고, 2vs2 축구 환경을 구성합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | MARL, Self-Play, ELO Rating, Cooperative / Competitive Env |
| 실습 환경 | `SoccerTwos` (Unity ML-Agents) |
| 주요 라이브러리 | `mlagents` |
| 멘토 자료 경로 | `unit-7/` |

</div>

---

### Unit 8 — Proximal Policy Optimization (PPO)

> 현업 표준 알고리즘 PPO 이론부터 구현까지

**Part 1 — PPO 기초 구현 (PyTorch)**

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | PPO, Clipped Surrogate Objective, GAE |
| 실습 환경 | `LunarLander-v2` |
| 주요 라이브러리 | `torch`, `gymnasium` |

</div>

**Part 2 — PPO 심화: VizDoom 적용 (Sample Factory)**

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | High-Throughput RL Pipeline, Sample Factory |
| 실습 환경 | `VizDoom` Health Gathering Supreme |
| 주요 라이브러리 | `sample-factory`, `vizdoom` |
| 멘토 자료 경로 | `unit-8/` |

</div>

---

## 👨‍🏫 멘토

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-SeonGyuJang-181717?style=flat-square&logo=github)](https://github.com/SeonGyuJang)

**고려대학교 세종캠퍼스 · T-SUM 멘토 (2026)**

</div>

---

## 📎 참고 자료

<div align="center">

| 링크 | 설명 |
|:---:|:---:|
| [🤗 HuggingFace Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) | 공식 강의 교재 |
| [📦 HuggingFace 공식 GitHub](https://github.com/huggingface/deep-rl-class) | 원본 실습 코드 및 노트북 |
| [🏫 고려대학교 세종캠퍼스](https://sejong.korea.ac.kr) | 주관 기관 |

</div>

---

<div align="center">

**© 2026 T-SUM Program · 고려대학교 세종캠퍼스 학생복지처 취창업지원센터**

*Tech Skill Up Mentoring · Powered by 🤗 HuggingFace Deep RL Course*

</div>
"""

# ── 진행도 자동 업데이트 스크립트 ──────────────────────────────────────────────
# 멘토용: note.md 또는 curriculum.md 존재 여부로 완료 판정
UPDATE_PROGRESS_PY = '''\
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
        f"| {icon} | **Unit {unit_num}** | {info[\'title\']} | {note_str} | {curr_str} |"
    )

table   = "\\n".join(rows)
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
    new_content = content.replace("\\n---\\n", f"\\n{progress_block}\\n---\\n", 1)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Mentor progress updated: {completed}/{total} ({pct}%)")
'''

GITHUB_ACTION_YML = """\
name: 📋 Auto Update Mentor Progress

on:
  push:
    paths:
      - 'unit-1/**'
      - 'unit-2/**'
      - 'unit-3/**'
      - 'unit-4/**'
      - 'unit-5/**'
      - 'unit-6/**'
      - 'unit-7/**'
      - 'unit-8/**'
  workflow_dispatch:

jobs:
  update-progress:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Run mentor progress update script
        run: python3 scripts/update_progress.py

      - name: Commit and push if changed
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          if git diff --staged --quiet; then
            echo "No changes to commit."
          else
            git commit -m "📋 [Auto] Mentor progress updated"
            git pull --rebase origin main
            git push origin main
          fi
"""

GITKEEP = ""

# ══════════════════════════════════════════════════════════════════════════════
# 2. Unit별 초기 파일 내용
# ══════════════════════════════════════════════════════════════════════════════

UNIT_INFO = {
    "unit-1": ("Introduction to Deep Reinforcement Learning",
                "LunarLander-v2", "stable-baselines3, gymnasium"),
    "unit-2": ("Introduction to Q-Learning",
                "FrozenLake-v1, Taxi-v3", "numpy, gymnasium"),
    "unit-3": ("Deep Q-Learning with Atari Games",
                "SpaceInvadersNoFrameskip-v4", "rl-baselines3-zoo, gymnasium[atari]"),
    "unit-4": ("Policy Gradient with PyTorch",
                "CartPole-v1, Pixelcopter-PLE-v0", "torch, gymnasium"),
    "unit-5": ("Introduction to Unity ML-Agents",
                "SnowballTarget, Pyramids", "mlagents"),
    "unit-6": ("Actor-Critic Methods with Robotics",
                "PyBullet Robotics Environments", "stable-baselines3, pybullet"),
    "unit-7": ("Multi-Agent Reinforcement Learning",
                "SoccerTwos (Unity ML-Agents)", "mlagents"),
    "unit-8": ("Proximal Policy Optimization (PPO)",
                "LunarLander-v2 / VizDoom Health Gathering Supreme",
                "torch, sample-factory, vizdoom"),
}

def make_note(unit_num: int, title: str, env: str, libs: str) -> str:
    """개념 정리본 템플릿"""
    return textwrap.dedent(f"""\
        # Unit {unit_num} — {title} : 개념 정리본

        > 멘티 배포용 개념 정리 노트입니다. 수업 전 작성 후 업로드하세요.

        ---

        ## 핵심 개념

        <!-- 이 Unit에서 반드시 이해해야 할 개념을 정리하세요 -->

        -
        -
        -

        ## 알고리즘 / 수식 정리

        <!-- 주요 알고리즘 흐름이나 수식을 정리하세요 -->

        ## 실습 요약

        | 항목 | 내용 |
        |:---:|:---:|
        | 실습 환경 | `{env}` |
        | 주요 라이브러리 | `{libs}` |

        ## 보충 자료

        - [HuggingFace Course Unit {unit_num}](https://huggingface.co/learn/deep-rl-course/unit{unit_num}/introduction)

        ## 멘토 메모

        <!-- 수업 중 멘티 반응, 보완할 설명 등 자유롭게 기록하세요 -->
    """)

def make_curriculum(unit_num: int, title: str) -> str:
    """수업 진행 계획 메모 템플릿"""
    return textwrap.dedent(f"""\
        # Unit {unit_num} — {title} : 수업 진행 계획

        ---

        ## 수업 목표

        <!-- 이번 Unit에서 멘티가 달성해야 할 목표를 작성하세요 -->

        1.
        2.
        3.

        ## 수업 순서

        | 순서 | 내용 | 예상 시간 |
        |:---:|---|:---:|
        | 1 | 개념 질문 및 복습 | 분 |
        | 2 | 실습 진행 | 분 |
        | 3 | 결과 공유 및 피드백 | 분 |

        ## 사전 학습 안내 (멘티용)

        <!-- 수업 전 멘티에게 안내할 사전 학습 내용을 작성하세요 -->

        - [ ]
        - [ ]

        ## 실습 포인트

        <!-- 실습 중 멘티가 특히 주의해야 할 부분을 작성하세요 -->

        ## 수업 후 기록

        <!-- 수업 진행 후 특이사항, 다음 수업 개선점 등을 기록하세요 -->
    """)

# ══════════════════════════════════════════════════════════════════════════════
# 3. 파일 생성 함수
# ══════════════════════════════════════════════════════════════════════════════

BASE = None

def write_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    rel = os.path.relpath(path, BASE)
    info(f"생성: {rel}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. 메인 실행
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    global BASE
    BASE = os.getcwd()

    print()
    print(c("  ╔══════════════════════════════════════════════════════╗", "36"))
    print(c("  ║   T-SUM Deep RL — 멘토 레포지토리 자동 생성 스크립트   ║", "36"))
    print(c("  ╚══════════════════════════════════════════════════════╝", "36"))

    if os.path.exists(os.path.join(BASE, ".github")):
        warn("이미 구조가 생성된 폴더입니다.")
        answer = input(c("  계속 진행하면 기존 파일이 덮어씌워집니다. 계속할까요? (y/N) : ", "33")).strip().lower()
        if answer != "y":
            print(c("\n  취소되었습니다.\n", "31"))
            sys.exit(0)

    head("① GitHub Actions 워크플로우 생성")
    write_file(
        os.path.join(BASE, ".github", "workflows", "update-progress.yml"),
        GITHUB_ACTION_YML,
    )

    head("② 진행도 업데이트 스크립트 생성")
    write_file(
        os.path.join(BASE, "scripts", "update_progress.py"),
        UPDATE_PROGRESS_PY,
    )

    head("③ Unit 폴더 생성 (unit-1 ~ unit-8)")
    for folder, (title, env, libs) in UNIT_INFO.items():
        unit_num = int(folder.split("-")[1])
        unit_dir = os.path.join(BASE, folder)
        write_file(os.path.join(unit_dir, ".gitkeep"), GITKEEP)
        write_file(os.path.join(unit_dir, "note.md"),
                   make_note(unit_num, title, env, libs))
        write_file(os.path.join(unit_dir, "curriculum.md"),
                   make_curriculum(unit_num, title))

    head("④ 메인 README.md 생성")
    write_file(os.path.join(BASE, "README.md"), README_CONTENT)

    head("⑤ .gitignore 생성")
    gitignore = textwrap.dedent("""\
        # Python
        __pycache__/
        *.py[cod]
        .env
        .venv/
        venv/

        # Jupyter
        .ipynb_checkpoints/

        # macOS
        .DS_Store

        # IDE
        .vscode/
        .idea/
    """)
    write_file(os.path.join(BASE, ".gitignore"), gitignore)

    done("멘토 레포지토리 구조 생성이 완료되었습니다!")
    print()
    print(c("  📁 생성된 위치:", "36"), c(os.path.abspath(BASE), "33"))
    print()
    print(c("  ─── 다음 단계 ───────────────────────────────────────────", "90"))
    print(c("  1. 이미 클론된 폴더 안에서 실행했다면 바로 push하면 됩니다:", "37"))
    print()
    print(c( "     git add .", "33"))
    print(c( "     git commit -m '📚 Initial commit: T-SUM Mentor Repo'", "33"))
    print(c( "     git push", "33"))
    print()
    print(c("  2. GitHub Settings → Actions → General →", "37"))
    print(c("     Workflow permissions → Read and write 로 설정하세요.", "37"))
    print()
    print(c("  3. 각 unit-N/note.md 와 curriculum.md 를 작성 후 push하면", "37"))
    print(c("     README 진행도가 자동으로 갱신됩니다.", "37"))
    print(c("  ─────────────────────────────────────────────────────────", "90"))
    print()


if __name__ == "__main__":
    main()