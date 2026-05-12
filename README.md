# Enterprise AI Skills for Antigravity

Antigravity-native consulting and PM workflows for structured strategy, executive communication, prioritization, meeting prep, deck narratives, document critique, and lightweight data/deck automation.

## Origin

This project is an Antigravity port of Sruthi Reddy's open-source [enterprise-ai-skills](https://github.com/sruthir28/enterprise-ai-skills) repository. The original project provides AI skills for enterprise professionals, including consulting frameworks, PM workflows, and practical tools primarily designed for Claude/LLM usage.

This repository adapts that source material into an Antigravity-native layout with slash-command workflows, token-efficient `SKILL.md` files, installer/uninstaller scripts, and a single canonical source tree under `antigravity/enterprise-ai/`.

## Install

```bash
npm install -g https://github.com/giljae/enterprise-ai-skills-antigravity
```

This will automatically validate the source tree and install the skills to:

```text
~/.gemini/antigravity/skills/enterprise-ai/
```

You can also manage the installation using the CLI tool:

```bash
enterprise-ai-skills install
enterprise-ai-skills uninstall --remove-backups
```

## Manual Install (Legacy)

If you prefer to install manually:

```bash
./scripts/install_antigravity.sh
```

## Uninstall

```bash
./scripts/uninstall_antigravity.sh
```

To also remove installer-created backups:

```bash
./scripts/uninstall_antigravity.sh --remove-backups
```

## Validate

```bash
python scripts/validate_antigravity_skills.py
```

## Quick Start

After installing, open Antigravity and call a command directly in chat:

```text
/decision-memo

Reader: VP Product
Decision: approve slipping v2 launch from May 15 to June 1
Deadline: today
Options: ship all and slip, cut AI tagging, slip full scope
Evidence: team is 400 engineering hours over capacity; 3 of 4 design partners can absorb the slip
```

For ambiguous requests, use the router:

```text
/enterprise-ai

I need to convince leadership to cut scope from our Q3 roadmap. Help me choose the right workflow.
```

## Commands

| Command | What it does |
|---|---|
| `/enterprise-ai` | Routes ambiguous business/strategy requests to the right sub-skill |
| `/scpr` | Structures an argument using Situation, Complication, Problem, Recommendation |
| `/issue-tree` | Breaks a problem into MECE branches and testable hypotheses |
| `/decision-memo` | Drafts a 1-page yes/no decision memo |
| `/storyline` | Builds claim-based slide titles and deck flow |
| `/prioritize` | Scores features or initiatives with PM prioritization frameworks |
| `/meeting-prep` | Creates pre-read, agenda, talking points, objections, and rebuttals |
| `/ai-use-case-score` | Scores personal AI use cases on Value x Feasibility x Safety |
| `/mckinsey-critic` | Reviews decks, memos, and strategies with a consulting-quality rubric |
| `/deck-pipeline` | Runs strategist, builder, critic, and fixer workflow for decks |
| `/data-insights` | Analyzes CSV/Excel files and produces plain-English insights |
| `/gamma-deck` | Generates a Gamma presentation from a storyline file |

## Usage Examples

### Structure A Strategy Argument

```text
/scpr

Situation: We have $15M ARR and 90% gross retention in agency project management.
Complication: AI-native competitors are reducing usage in our core workflows.
Problem: How do we return to 25% growth in 12 months?
Recommendation: Reposition around AI-augmented agency operations.
```

### Break Down A Problem

```text
/issue-tree

Governing question: How can we increase self-serve revenue by 40% in 12 months?
Known constraints: no headcount increase, pricing changes allowed, onboarding can change.
```

### Prioritize A Roadmap

```text
/prioritize

Use RICE to rank these: Slack integration, mobile app, custom dashboards, API docs.
Context: B2B SaaS, 8K users, 4 engineers, goal is expansion revenue this quarter.
```

### Prepare For A Meeting

```text
/meeting-prep

Attendees: VP Eng, PM lead
Length: 30 minutes
Topic: move v2 launch from May 15 to June 1
Outcome: both approve the slip by end of meeting
Evidence: 400-hour capacity gap, Q1 burnout survey at 4/10
```

### Build A Deck Narrative

```text
/storyline

Audience: board
Goal: approve investment in enterprise onboarding
Topic: activation gap in enterprise accounts
Known data: enterprise activation is 42% vs SMB 68%; onboarding tickets are up 35% QoQ
Target length: 10 slides
```

### Review Before Sending

```text
/mckinsey-critic

Review this decision memo for structure, evidence, and whether the ask is sharp enough:
[paste memo]
```

### Score Personal AI Use Cases

```text
/ai-use-case-score

My weekly tasks: status updates, customer call synthesis, roadmap grooming, exec review prep.
Goal: save 5 hours per week without exposing customer PII.
```

### Analyze Data

```text
/data-insights

Analyze ./data/q1_pipeline.csv and summarize target performance, trend, unusual changes, and best/worst segments.
```

### Generate A Gamma Deck

```text
/gamma-deck

Input file: ./storyline.txt
Output: board_update.pptx
Theme: Chisel
Audience: executives
```

## Repository Layout

```text
antigravity/enterprise-ai/    Canonical Antigravity skill source
scripts/                      Install, uninstall, and validation automation
docs/                         Porting notes and implementation plan
```

## Scripted Workflows

`/data-insights` uses:

```text
antigravity/enterprise-ai/data-insights/scripts/analyze_data.py
```

`/gamma-deck` uses:

```text
antigravity/enterprise-ai/gamma-deck/scripts/gamma_deck_generator.py
```

Set `GAMMA_API_KEY` in the environment before running `/gamma-deck`.

## License

MIT. See `LICENSE`.
