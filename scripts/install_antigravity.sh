#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/antigravity/enterprise-ai"
TARGET_ROOT="${ANTIGRAVITY_SKILLS_DIR:-$HOME/.gemini/antigravity/skills}"
TARGET_DIR="$TARGET_ROOT/enterprise-ai"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Source suite not found: $SOURCE_DIR" >&2
  exit 1
fi

python "$ROOT_DIR/scripts/validate_antigravity_skills.py"

mkdir -p "$TARGET_ROOT"

if [[ -e "$TARGET_DIR" ]]; then
  BACKUP_DIR="$TARGET_DIR.backup.$(date +%Y%m%d%H%M%S)"
  echo "Backing up existing installation to $BACKUP_DIR"
  mv "$TARGET_DIR" "$BACKUP_DIR"
fi

cp -R "$SOURCE_DIR" "$TARGET_DIR"

echo "Installed Enterprise AI skills to $TARGET_DIR"
echo "Available commands: /enterprise-ai, /scpr, /issue-tree, /decision-memo, /storyline, /prioritize, /meeting-prep, /ai-use-case-score, /mckinsey-critic, /deck-pipeline, /data-insights, /gamma-deck"
