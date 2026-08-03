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

### `███████████████░░░░░` &nbsp; 6 / 8 Units &nbsp; **75%**

🕐 마지막 업데이트: 2026-08-03 22:33 KST

<br>

| 상태 | Unit | 주제 | 실습 파일 | 노션 정리본 |
|:---:|:---:|:---:|:---:|:---:|
| ✅ | **Unit 1** | Intro to Deep RL | ✅ | ✅ |
| ✅ | **Unit 2** | Q-Learning | ✅ | ✅ |
| ✅ | **Unit 3** | Deep Q-Learning (DQN) | ✅ | ✅ |
| ✅ | **Unit 4** | Policy Gradient (REINFORCE) | ✅ | ✅ |
| ✅ | **Unit 5** | Unity ML-Agents | ✅ | ✅ |
| ✅ | **Unit 6** | Actor-Critic (A2C) | ✅ | ✅ |
| ⬜ | **Unit 7** | Multi-Agent RL (MARL) | ❌ | ❌ |
| ⬜ | **Unit 8** | PPO | ❌ | ❌ |

</div>

> 📌 각 Unit 폴더에 실습 파일(`.ipynb`/`.py`)과 노션 링크(`notion.txt`)를 업로드하면 진행도가 자동으로 갱신됩니다.

---
<!-- PROGRESS_END -->

## 📌 레포지토리 소개

본 레포지토리는 **고려대학교 세종캠퍼스 학생복지처 취창업지원센터**가 주관하는 **T-SUM(Tech Skill Up Mentoring) 프로그램**의 **멘토 자료 저장소**입니다.

[HuggingFace Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)를 기반으로 Unit 1~8의 **실습 예시 코드**와 **개념 정리본(Notion) 링크**를 제공하며, 멘티들의 학습을 지원합니다.

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
│   ├── 📄 notion.txt                  # Notion 정리본 링크
│   ├── 📓 (실습 파일.ipynb)            # 실습 예시 코드
│   └── 📄 memo.md                     # 자유 기입 메모
├── 📁 unit-2/ ~ unit-8/               # 동일한 구조
│
└── 📄 README.md
```

> `notion.txt` 에 Notion 링크를 붙여넣고, 실습 파일(`.ipynb` / `.py`)을 업로드하면 진행도가 자동으로 갱신됩니다.

---

## 📚 커리큘럼

### Unit 1 — Introduction to Deep Reinforcement Learning

> 강화학습의 기초 개념과 첫 번째 에이전트 구현

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | RL Framework, MDP, Agent-Environment Interaction |
| 실습 환경 | `LunarLander-v2` |
| 주요 라이브러리 | `stable-baselines3`, `gymnasium` |
| 자료 경로 | `unit-1/` |

</div>

---

### Unit 2 — Introduction to Q-Learning

> 가치 기반 학습의 핵심: Q-테이블 직접 구현

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Q-Table, Bellman Equation, ε-Greedy Policy, TD Learning |
| 실습 환경 | `FrozenLake-v1`, `Taxi-v3` |
| 주요 라이브러리 | `numpy`, `gymnasium` |
| 자료 경로 | `unit-2/` |

</div>

---

### Unit 3 — Deep Q-Learning with Atari Games

> 신경망을 결합한 DQN으로 Atari 게임 정복

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | DQN, Experience Replay, Fixed Q-Target, CNN |
| 실습 환경 | `SpaceInvadersNoFrameskip-v4` |
| 주요 라이브러리 | `rl-baselines3-zoo`, `gymnasium[atari]` |
| 자료 경로 | `unit-3/` |

</div>

---

### Unit 4 — Policy Gradient with PyTorch

> 정책 직접 최적화: REINFORCE 알고리즘 구현

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Policy Gradient, REINFORCE, Stochastic Policy |
| 실습 환경 | `CartPole-v1`, `Pixelcopter-PLE-v0` |
| 주요 라이브러리 | `torch`, `gymnasium` |
| 자료 경로 | `unit-4/` |

</div>

---

### Unit 5 — Introduction to Unity ML-Agents

> Unity 게임 엔진 기반 강화학습 환경 실습

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | ML-Agents Toolkit, Unity Environment |
| 실습 환경 | `SnowballTarget`, `Pyramids` |
| 주요 라이브러리 | `mlagents` |
| 자료 경로 | `unit-5/` |

</div>

---

### Unit 6 — Actor-Critic Methods with Robotics

> 가치 기반 + 정책 기반의 결합: A2C 알고리즘

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | Actor-Critic, A2C, Advantage Function, Continuous Action Space |
| 실습 환경 | `PyBullet` Robotics Environments |
| 주요 라이브러리 | `stable-baselines3`, `pybullet` |
| 자료 경로 | `unit-6/` |

</div>

---

### Unit 7 — Multi-Agent Reinforcement Learning

> 다수의 에이전트가 협력·경쟁하는 MARL

<div align="center">

| 항목 | 내용 |
|:---:|:---:|
| 핵심 개념 | MARL, Self-Play, ELO Rating, Cooperative / Competitive Env |
| 실습 환경 | `SoccerTwos` (Unity ML-Agents) |
| 주요 라이브러리 | `mlagents` |
| 자료 경로 | `unit-7/` |

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
| 자료 경로 | `unit-8/` |

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
