"""
╔══════════════════════════════════════════════════════════════════╗
║         T-SUM Deep RL — GitHub 레포지토리 자동 생성 스크립트         ║
║    실행하면 현재 디렉토리에 T-SUM-Deep-RL-Course 폴더가 만들어집니다   ║
╚══════════════════════════════════════════════════════════════════╝

사용법:
    python setup_tsum_repo.py

Python 3.8 이상, 외부 라이브러리 불필요 (표준 라이브러리만 사용)
"""

import os
import sys
import textwrap

# ══════════════════════════════════════════════════════════════════════════════
# 0. 색상 출력 헬퍼
# ══════════════════════════════════════════════════════════════════════════════

def c(text, code):
    """ANSI 색상 출력 (Windows cmd 미지원 시 색상 제거)"""
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

**Tech Skill Up Mentoring — HuggingFace Deep RL Course 실습 포트폴리오**

고려대학교 세종캠퍼스 학생복지처 취창업지원센터

</div>

---

<!-- PROGRESS_START -->
## 📊 학습 진행 현황

<div align="center">

### `░░░░░░░░░░░░░░░░░░░░` &nbsp; 0 / 8 Units &nbsp; **0%**

**수료 상태**: ⏳ 진행 중 (0%) &nbsp;｜&nbsp; 🕐 마지막 업데이트: -

<br>

| 상태 | Unit | 주제 | 실습 환경 | 제출 여부 |
|:---:|:---:|:---:|:---:|:---:|
| ⬜ | **Unit 1** | Intro to Deep RL | `LunarLander` | 미제출 |
| ⬜ | **Unit 2** | Q-Learning | `FrozenLake / Taxi` | 미제출 |
| ⬜ | **Unit 3** | Deep Q-Learning (DQN) | `Space Invaders` | 미제출 |
| ⬜ | **Unit 4** | Policy Gradient (REINFORCE) | `CartPole / Pixelcopter` | 미제출 |
| ⬜ | **Unit 5** | Unity ML-Agents | `SnowballTarget / Pyramids` | 미제출 |
| ⬜ | **Unit 6** | Actor-Critic (A2C) | `PyBullet Robotics` | 미제출 |
| ⬜ | **Unit 7** | Multi-Agent RL (MARL) | `Soccer 2v2` | 미제출 |
| ⬜ | **Unit 8** | PPO | `LunarLander / VizDoom` | 미제출 |

</div>

> 📌 멘토가 각 Unit 폴더에 실습 파일(`.ipynb` / `.py`)을 업로드하면 진행도가 자동으로 갱신됩니다.

---
<!-- PROGRESS_END -->

## 📌 프로젝트 소개

본 레포지토리는 **고려대학교 세종캠퍼스 학생복지처 취창업지원센터**가 주관하는 **T-SUM(Tech Skill Up Mentoring) 프로그램**의 실습 포트폴리오입니다.

**T-SUM**은 Python을 활용한 데이터 분석 및 인공지능 멘토링 프로그램으로, 멘토-멘티 간 1:N 구조로 운영됩니다. 본 프로그램에서는 [HuggingFace Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)를 교재로 채택하여, **Flipped Class** 방식으로 개념은 자율 학습, 실습은 함께 진행합니다.

본 저장소는 Unit 1~8에 걸쳐 학습한 Deep RL 알고리즘의 **실습 코드, 학습 결과, 훈련된 에이전트**를 체계적으로 기록하며, HuggingFace 공식 수료증 취득을 최종 목표로 합니다.

---

## 🗂️ 레포지토리 구조

```
📦 T-SUM-Deep-RL-Course
│
├── 📁 .github/
│   └── 📁 workflows/
│       └── ⚙️  update-progress.yml     # 진행도 자동 업데이트 Action
│
├── 📁 scripts/
│   └── 🐍 update_progress.py          # 진행도 계산 스크립트
│
├── 📁 certificate/                    # 수료증 이미지 저장 폴더
│
├── 📁 unit-1/                         # Introduction to Deep RL
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

> 각 `unit-N/` 폴더에 `.ipynb` 또는 `.py` 실습 파일이 업로드되면, GitHub Actions가 자동으로 위 진행도를 갱신합니다.

---

## 📚 커리큘럼

### Unit 1 — Introduction to Deep Reinforcement Learning

> 강화학습의 기초 개념과 첫 번째 에이전트 구현

강화학습(RL)의 전반적인 학습 프레임워크를 이해하고, 에이전트(Agent)·환경(Environment)·보상(Reward)·정책(Policy) 등 핵심 개념을 학습합니다. Stable-Baselines3 라이브러리를 활용해 LunarLander 환경에서 첫 번째 RL 에이전트를 학습시키고 HuggingFace Hub에 업로드합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | RL Framework, MDP, Agent-Environment Interaction |
| 실습 환경 | `LunarLander-v2` |
| 주요 라이브러리 | `stable-baselines3`, `gymnasium` |
| 실습 파일 경로 | `unit-1/` |

</div>

---

### Unit 2 — Introduction to Q-Learning

> 가치 기반 학습의 핵심: Q-테이블 직접 구현

Markov Decision Process(MDP)와 벨만 방정식(Bellman Equation)을 이해하고, Monte Carlo와 Temporal Difference(TD) 학습을 비교합니다. Q-Learning 에이전트를 라이브러리 없이 처음부터(scratch) 구현합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Q-Table, Bellman Equation, ε-Greedy Policy, TD Learning |
| 실습 환경 | `FrozenLake-v1`, `Taxi-v3` |
| 주요 라이브러리 | `numpy`, `gymnasium` |
| 실습 파일 경로 | `unit-2/` |

</div>

---

### Unit 3 — Deep Q-Learning with Atari Games

> 신경망을 결합한 DQN으로 Atari 게임 정복

Q-Learning의 한계를 파악하고 Deep Q-Network(DQN)의 등장 배경을 학습합니다. Experience Replay, Fixed Q-Target 등 DQN의 핵심 안정화 기법을 이해하고, CNN 기반 에이전트를 훈련합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | DQN, Experience Replay, Fixed Q-Target, CNN |
| 실습 환경 | `SpaceInvadersNoFrameskip-v4` |
| 주요 라이브러리 | `rl-baselines3-zoo`, `gymnasium[atari]` |
| 실습 파일 경로 | `unit-3/` |

</div>

---

### Unit 4 — Policy Gradient with PyTorch

> 정책 직접 최적화: REINFORCE 알고리즘 구현

Policy-Based 방법론이 Value-Based 대비 갖는 장점을 이해하고, Policy Gradient 이론을 학습합니다. PyTorch를 활용해 REINFORCE 알고리즘을 직접 구현합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Policy Gradient, REINFORCE, Stochastic Policy |
| 실습 환경 | `CartPole-v1`, `Pixelcopter-PLE-v0` |
| 주요 라이브러리 | `torch`, `gymnasium` |
| 실습 파일 경로 | `unit-4/` |

</div>

---

### Unit 5 — Introduction to Unity ML-Agents

> Unity 게임 엔진 기반 강화학습 환경 실습

Unity ML-Agents 툴킷의 구조와 활용법을 이해하고, 3D 물리 시뮬레이션 환경에서 에이전트를 학습시킵니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | ML-Agents Toolkit, Unity Environment |
| 실습 환경 | `SnowballTarget`, `Pyramids` |
| 주요 라이브러리 | `mlagents` |
| 실습 파일 경로 | `unit-5/` |

</div>

---

### Unit 6 — Actor-Critic Methods with Robotics

> 가치 기반 + 정책 기반의 결합: A2C 알고리즘

Actor-Critic 아키텍처의 구조와 작동 원리를 이해하고 Advantage Function 개념을 학습합니다. 로봇 제어 연속 행동 공간 환경에 적용합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Actor-Critic, A2C, Advantage Function, Continuous Action Space |
| 실습 환경 | `PyBullet` Robotics Environments |
| 주요 라이브러리 | `stable-baselines3`, `pybullet` |
| 실습 파일 경로 | `unit-6/` |

</div>

---

### Unit 7 — Multi-Agent Reinforcement Learning

> 다수의 에이전트가 협력·경쟁하는 MARL

Multi-Agent RL(MARL)의 핵심 개념과 Self-Play 전략을 이해합니다. ML-Agents를 활용해 에이전트끼리 대결하며 스스로 실력을 키우는 2vs2 축구 환경을 구성합니다.

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | MARL, Self-Play, ELO Rating, Cooperative / Competitive Env |
| 실습 환경 | `SoccerTwos` (Unity ML-Agents) |
| 주요 라이브러리 | `mlagents` |
| 실습 파일 경로 | `unit-7/` |

</div>

---

### Unit 8 — Proximal Policy Optimization (PPO)

> 현업 표준 알고리즘 PPO 이론부터 구현까지

현재 가장 널리 사용되는 Deep RL 알고리즘인 PPO를 학습합니다. Clipped Surrogate Objective로 안정적인 정책 업데이트를 구현하고, 고효율 학습 파이프라인까지 경험합니다.

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
| 실습 파일 경로 | `unit-8/` |

</div>

---

## 🏅 HuggingFace 공식 수료증

> HuggingFace Deep RL Course는 전체 과제의 **80% 이상** 완료 시 공식 수료증을 무료로 발급합니다.
> **100% 완료** 시 우수 수료증(Certificate of Honors)이 발급됩니다.

<div align="center">

| 등급 | 조건 | 비고 |
|:---:|:---:|:---:|
| 🎓 Certificate of Completion | 전체 과제 80% 이상 완료 | HuggingFace 공식 발급 |
| 🏅 Certificate of Honors | 전체 과제 100% 완료 | HuggingFace 공식 발급 |

</div>

### 📜 수료증

<!-- 수료증 발급 후 certificate/certificate.png 에 이미지를 업로드하고 아래 주석을 해제하세요 -->
<!--
<div align="center">
  <img src="certificate/certificate.png" alt="HuggingFace Deep RL Certificate" width="700"/>
</div>
-->

<div align="center">
  <sub>🔒 수료증은 과정 완료 후 이 자리에 업로드될 예정입니다.</sub>
</div>

---

## 👨‍🏫 멘토

<div align="center">

**본 프로그램의 멘토 GitHub 프로필에서 정리본 및 참고 자료를 확인할 수 있습니다.**

[→ 멘토 GitHub 바로가기](https://github.com/SeonGyuJang)

</div>

---

## 📎 참고 자료

<div align="center">

| 링크 | 설명 |
|:---:|:---:|
| [🤗 HuggingFace Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) | 공식 강의 교재 |
| [📦 HuggingFace 공식 GitHub](https://github.com/huggingface/deep-rl-class) | 원본 실습 코드 및 노트북 |
| [🏫 고려대학교 세종캠퍼스](https://sejong.korea.ac.kr) | 주관 기관 |
| [📜 수료증 발급 안내](https://huggingface.co/learn/deep-rl-course/unit0/introduction#the-certification-process) | HuggingFace 수료증 안내 페이지 |

</div>

---

<div align="center">

**© 2026 T-SUM Program · 고려대학교 세종캠퍼스 학생복지처 취창업지원센터**

*Tech Skill Up Mentoring · Powered by 🤗 HuggingFace Deep RL Course*

</div>
"""

UPDATE_PROGRESS_PY = '''\
"""
T-SUM Progress Auto-Updater
----------------------------
unit-1 ~ unit-8 폴더에 .ipynb / .py 파일이 존재하는지 확인하고,
README.md 의 <!-- PROGRESS_START --> ~ <!-- PROGRESS_END --> 블록을 자동 갱신합니다.
"""

import os
import re
from datetime import datetime, timezone, timedelta

# ── 설정 ──────────────────────────────────────────────────────────────────────
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

VALID_EXTENSIONS = {".ipynb", ".py"}
README_PATH = "README.md"
KST = timezone(timedelta(hours=9))

# ── 파일 감지 ─────────────────────────────────────────────────────────────────
def has_submission(folder: str) -> bool:
    if not os.path.isdir(folder):
        return False
    for fname in os.listdir(folder):
        if os.path.splitext(fname)[1].lower() in VALID_EXTENSIONS:
            return True
    return False

# ── 진행도 계산 ───────────────────────────────────────────────────────────────
statuses  = {k: has_submission(k) for k in UNITS}
completed = sum(statuses.values())
total     = len(UNITS)
pct       = int(completed / total * 100)

# ── HuggingFace 수료 기준 ─────────────────────────────────────────────────────
if pct == 100:
    cert_badge = "🏅 **Honors** (100%)"
elif pct >= 80:
    cert_badge = "🎓 **Completion** (80%+)"
else:
    cert_badge = f"⏳ 진행 중 ({pct}%)"

# ── 진행 바 생성 (GitHub Markdown 호환) ──────────────────────────────────────
BAR_LEN = 20
filled  = round(pct / 100 * BAR_LEN)
bar     = "█" * filled + "░" * (BAR_LEN - filled)

# ── Unit 테이블 생성 ──────────────────────────────────────────────────────────
rows = []
for folder, info in UNITS.items():
    done     = statuses[folder]
    icon     = "✅" if done else "⬜"
    status   = "완료"  if done else "미제출"
    unit_num = folder.replace("unit-", "")
    rows.append(
        f"| {icon} | **Unit {unit_num}** | {info[\'title\']} | `{info[\'env\']}` | {status} |"
    )

table   = "\\n".join(rows)
now_kst = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

# ── 삽입할 마크다운 블록 ──────────────────────────────────────────────────────
progress_block = f"""<!-- PROGRESS_START -->
## 📊 학습 진행 현황

<div align="center">

### `{bar}` &nbsp; {completed} / {total} Units &nbsp; **{pct}%**

**수료 상태**: {cert_badge} &nbsp;｜&nbsp; 🕐 마지막 업데이트: {now_kst}

<br>

| 상태 | Unit | 주제 | 실습 환경 | 제출 여부 |
|:---:|:---:|:---:|:---:|:---:|
{table}

</div>

> 📌 멘토가 각 Unit 폴더에 실습 파일(`.ipynb` / `.py`)을 업로드하면 진행도가 자동으로 갱신됩니다.

---
<!-- PROGRESS_END -->"""

# ── README 갱신 ───────────────────────────────────────────────────────────────
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"<!-- PROGRESS_START -->.*?<!-- PROGRESS_END -->"
if re.search(pattern, content, flags=re.DOTALL):
    new_content = re.sub(pattern, progress_block, content, flags=re.DOTALL)
else:
    new_content = content.replace("\\n---\\n", f"\\n{progress_block}\\n---\\n", 1)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Progress updated: {completed}/{total} ({pct}%)")
'''

GITHUB_ACTION_YML = """\
name: 📊 Auto Update Progress

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

      - name: Run progress update script
        run: python3 scripts/update_progress.py

      - name: Commit and push if changed
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          if git diff --staged --quiet; then
            echo "No changes to commit."
          else
            git commit -m "📊 [Auto] Progress updated"
            git pull --rebase origin main
            git push origin main
          fi
"""

GITKEEP = ""


CERT_PLACEHOLDER = """\
# 📜 수료증 폴더

HuggingFace Deep RL Course 공식 수료증을 이 폴더에 저장하세요.

## 업로드 방법
1. HuggingFace에서 수료증 이미지를 다운로드합니다.
2. 파일명을 `certificate.png` 로 저장합니다.
3. 이 폴더(`certificate/`)에 업로드합니다.
4. `README.md` 의 수료증 섹션에서 주석(`<!-- -->`)을 제거합니다.

그러면 README에 수료증 이미지가 자동으로 표시됩니다.
"""

# ══════════════════════════════════════════════════════════════════════════════
# 2. 생성할 구조 정의
# ══════════════════════════════════════════════════════════════════════════════

REPO_NAME = "T-SUM-Deep-RL-Course"

UNIT_READMES = {
    "unit-1": ("Introduction to Deep Reinforcement Learning",
                "LunarLander-v2",
                "stable-baselines3, gymnasium"),
    "unit-2": ("Introduction to Q-Learning",
                "FrozenLake-v1, Taxi-v3",
                "numpy, gymnasium"),
    "unit-3": ("Deep Q-Learning with Atari Games",
                "SpaceInvadersNoFrameskip-v4",
                "rl-baselines3-zoo, gymnasium[atari]"),
    "unit-4": ("Policy Gradient with PyTorch",
                "CartPole-v1, Pixelcopter-PLE-v0",
                "torch, gymnasium"),
    "unit-5": ("Introduction to Unity ML-Agents",
                "SnowballTarget, Pyramids",
                "mlagents"),
    "unit-6": ("Actor-Critic Methods with Robotics",
                "PyBullet Robotics Environments",
                "stable-baselines3, pybullet"),
    "unit-7": ("Multi-Agent Reinforcement Learning",
                "SoccerTwos (Unity ML-Agents)",
                "mlagents"),
    "unit-8": ("Proximal Policy Optimization (PPO)",
                "LunarLander-v2 / VizDoom Health Gathering Supreme",
                "torch, sample-factory, vizdoom"),
}

def make_unit_readme(unit_num: int, title: str, env: str, libs: str) -> str:
    return textwrap.dedent(f"""\
        # Unit {unit_num} — {title}

        ## 실습 환경
        `{env}`

        ## 주요 라이브러리
        `{libs}`

        ## 실습 파일
        실습 완료 후 `.ipynb` 또는 `.py` 파일을 이 폴더에 업로드하세요.

        ## 참고 링크
        - [HuggingFace Course Unit {unit_num}](https://huggingface.co/learn/deep-rl-course/unit{unit_num}/introduction)
    """)

# ══════════════════════════════════════════════════════════════════════════════
# 3. 폴더 & 파일 생성 함수
# ══════════════════════════════════════════════════════════════════════════════

def write_file(path: str, content: str, base_override: str = None) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    rel = os.path.relpath(path, base_override or BASE)
    info(f"생성: {rel}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. 메인 실행
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    global BASE

    BASE = os.getcwd()

    print()
    print(c("  ╔══════════════════════════════════════════════════════╗", "36"))
    print(c("  ║    T-SUM Deep RL — 레포지토리 자동 생성 스크립트       ║", "36"))
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
    for folder, (title, env, libs) in UNIT_READMES.items():
        unit_num = int(folder.split("-")[1])
        unit_dir = os.path.join(BASE, folder)
        write_file(os.path.join(unit_dir, ".gitkeep"), GITKEEP)
        write_file(
            os.path.join(unit_dir, "README.md"),
            make_unit_readme(unit_num, title, env, libs),
        )

    head("④ 수료증 폴더 생성")
    write_file(os.path.join(BASE, "certificate", ".gitkeep"), GITKEEP)
    write_file(os.path.join(BASE, "certificate", "README.md"), CERT_PLACEHOLDER)

    head("⑤ 메인 README.md 생성")
    write_file(os.path.join(BASE, "README.md"), README_CONTENT)

    head("⑥ .gitignore 생성")
    gitignore = textwrap.dedent("""\
        # Python
        __pycache__/
        *.py[cod]
        *.egg-info/
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

        # RL 학습 결과물 (용량이 클 경우 제외)
        # logs/
        # models/
    """)
    write_file(os.path.join(BASE, ".gitignore"), gitignore)

    done("레포지토리 구조 생성이 완료되었습니다!")
    print()
    print(c("  📁 생성된 위치:", "36"), c(os.path.abspath(BASE), "33"))
    print()
    print(c("  ─── 다음 단계 ───────────────────────────────────────────", "90"))
    print(c("  1. GitHub에서 새 레포지토리를 생성합니다.", "37"))
    print(c("  2. 이미 클론된 폴더 안에서 실행했다면 바로 push하면 됩니다:", "37"))
    print()
    print(c( "     git add .", "33"))
    print(c( "     git commit -m '🎉 Initial commit: T-SUM Deep RL Portfolio'", "33"))
    print(c( "     git push", "33"))
    print()
    print(c("     ── 새 레포를 처음 만드는 경우 ──", "90"))
    print(c( "     git init", "33"))
    print(c( "     git add .", "33"))
    print(c( "     git commit -m '🎉 Initial commit: T-SUM Deep RL Portfolio'", "33"))
    print(c( "     git branch -M main", "33"))
    print(c( "     git remote add origin https://github.com/[본인ID]/T-SUM-Deep-RL-Course.git", "33"))
    print(c( "     git push -u origin main", "33"))
    print()
    print(c("  3. 수료증 발급 후 certificate/certificate.png 를 업로드하세요.", "37"))
    print(c("  ─────────────────────────────────────────────────────────", "90"))
    print()


if __name__ == "__main__":
    main()
