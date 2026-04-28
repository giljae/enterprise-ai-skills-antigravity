# Antigravity용 Enterprise AI Skills

구조화된 전략, 임원 커뮤니케이션, 우선순위 결정, 회의 준비, 덱 내러티브, 문서 리뷰, 간단한 데이터/덱 자동화를 위한 Antigravity 네이티브 컨설팅 및 PM 워크플로입니다.

## 원천

이 프로젝트는 Sruthi Reddy의 오픈소스 [enterprise-ai-skills](https://github.com/sruthir28/enterprise-ai-skills) 저장소를 Antigravity용으로 포팅한 것입니다. 원본 프로젝트는 엔터프라이즈 전문가를 위한 AI 스킬 모음으로, 컨설팅 프레임워크, PM 워크플로, 실무 도구를 Claude/LLM 사용 방식에 맞게 제공합니다.

이 저장소는 해당 원천 자료를 Antigravity 네이티브 구조로 재구성했습니다. slash-command 워크플로, 토큰 효율적인 `SKILL.md`, 설치/제거 스크립트, `antigravity/enterprise-ai/` 단일 canonical source tree를 제공합니다.

## 설치

```bash
./scripts/install_antigravity.sh
```

이 명령은 소스 트리를 검증하고, 기존 설치본이 있으면 백업한 뒤, 다음 경로에 설치합니다.

```text
~/.gemini/antigravity/skills/enterprise-ai/
```

## 제거

```bash
./scripts/uninstall_antigravity.sh
```

설치 스크립트가 만든 백업까지 함께 제거하려면:

```bash
./scripts/uninstall_antigravity.sh --remove-backups
```

## 검증

```bash
python scripts/validate_antigravity_skills.py
```

## 빠른 시작

설치 후 Antigravity 채팅에서 명령어를 직접 호출합니다.

```text
/decision-memo

Reader: VP Product
Decision: approve slipping v2 launch from May 15 to June 1
Deadline: today
Options: ship all and slip, cut AI tagging, slip full scope
Evidence: team is 400 engineering hours over capacity; 3 of 4 design partners can absorb the slip
```

어떤 워크플로를 써야 할지 애매하면 라우터를 사용합니다.

```text
/enterprise-ai

I need to convince leadership to cut scope from our Q3 roadmap. Help me choose the right workflow.
```

## 명령어

| 명령어 | 기능 |
|---|---|
| `/enterprise-ai` | 모호한 비즈니스/전략 요청을 적절한 하위 스킬로 라우팅 |
| `/scpr` | Situation, Complication, Problem, Recommendation 구조로 논리 구성 |
| `/issue-tree` | 문제를 MECE 브랜치와 검증 가능한 가설로 분해 |
| `/decision-memo` | 1페이지 yes/no 의사결정 메모 작성 |
| `/storyline` | 주장형 슬라이드 제목과 덱 흐름 구성 |
| `/prioritize` | PM 우선순위 프레임워크로 기능 또는 이니셔티브 점수화 |
| `/meeting-prep` | pre-read, agenda, talking points, objections, rebuttals 작성 |
| `/ai-use-case-score` | 개인 AI use case를 Value x Feasibility x Safety로 점수화 |
| `/mckinsey-critic` | 컨설팅 품질 기준으로 덱, 메모, 전략 리뷰 |
| `/deck-pipeline` | 덱을 위한 strategist, builder, critic, fixer 워크플로 실행 |
| `/data-insights` | CSV/Excel 파일을 분석하고 쉬운 영어 인사이트 생성 |
| `/gamma-deck` | storyline 파일에서 Gamma 프레젠테이션 생성 |

## 사용 예시

### 전략 논리 구조화

```text
/scpr

Situation: We have $15M ARR and 90% gross retention in agency project management.
Complication: AI-native competitors are reducing usage in our core workflows.
Problem: How do we return to 25% growth in 12 months?
Recommendation: Reposition around AI-augmented agency operations.
```

### 문제 분해

```text
/issue-tree

Governing question: How can we increase self-serve revenue by 40% in 12 months?
Known constraints: no headcount increase, pricing changes allowed, onboarding can change.
```

### 로드맵 우선순위 결정

```text
/prioritize

Use RICE to rank these: Slack integration, mobile app, custom dashboards, API docs.
Context: B2B SaaS, 8K users, 4 engineers, goal is expansion revenue this quarter.
```

### 회의 준비

```text
/meeting-prep

Attendees: VP Eng, PM lead
Length: 30 minutes
Topic: move v2 launch from May 15 to June 1
Outcome: both approve the slip by end of meeting
Evidence: 400-hour capacity gap, Q1 burnout survey at 4/10
```

### 덱 내러티브 만들기

```text
/storyline

Audience: board
Goal: approve investment in enterprise onboarding
Topic: activation gap in enterprise accounts
Known data: enterprise activation is 42% vs SMB 68%; onboarding tickets are up 35% QoQ
Target length: 10 slides
```

### 발송 전 리뷰

```text
/mckinsey-critic

Review this decision memo for structure, evidence, and whether the ask is sharp enough:
[paste memo]
```

### 개인 AI use case 점수화

```text
/ai-use-case-score

My weekly tasks: status updates, customer call synthesis, roadmap grooming, exec review prep.
Goal: save 5 hours per week without exposing customer PII.
```

### 데이터 분석

```text
/data-insights

Analyze ./data/q1_pipeline.csv and summarize target performance, trend, unusual changes, and best/worst segments.
```

### Gamma 덱 생성

```text
/gamma-deck

Input file: ./storyline.txt
Output: board_update.pptx
Theme: Chisel
Audience: executives
```

## 저장소 구조

```text
antigravity/enterprise-ai/    표준 Antigravity 스킬 소스
scripts/                      설치, 제거, 검증 자동화
docs/                         포팅 노트와 구현 플랜
```

## 스크립트 기반 워크플로

`/data-insights`는 다음 스크립트를 사용합니다.

```text
antigravity/enterprise-ai/data-insights/scripts/analyze_data.py
```

`/gamma-deck`는 다음 스크립트를 사용합니다.

```text
antigravity/enterprise-ai/gamma-deck/scripts/gamma_deck_generator.py
```

`/gamma-deck`를 실행하기 전에 환경변수 `GAMMA_API_KEY`를 설정해야 합니다.

## 라이선스

MIT. `LICENSE`를 참고하세요.
