#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${ANTIGRAVITY_SKILLS_DIR:-$HOME/.gemini/antigravity/skills}"
TARGET_DIR="$TARGET_ROOT/enterprise-ai"
REMOVE_BACKUPS=false

usage() {
  cat <<'USAGE'
Usage: ./scripts/uninstall_antigravity.sh [--remove-backups]

Removes the installed Enterprise AI Antigravity skill suite from:
  ${ANTIGRAVITY_SKILLS_DIR:-$HOME/.gemini/antigravity/skills}/enterprise-ai

Options:
  --remove-backups   Also remove enterprise-ai.backup.* directories
  -h, --help         Show this help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --remove-backups)
      REMOVE_BACKUPS=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -d "$TARGET_DIR" ]]; then
  rm -rf "$TARGET_DIR"
  echo "Removed $TARGET_DIR"
else
  echo "No installed Enterprise AI suite found at $TARGET_DIR"
fi

if [[ "$REMOVE_BACKUPS" == "true" ]]; then
  shopt -s nullglob
  backups=("$TARGET_ROOT"/enterprise-ai.backup.*)
  if [[ ${#backups[@]} -eq 0 ]]; then
    echo "No Enterprise AI backup directories found."
  else
    rm -rf "${backups[@]}"
    echo "Removed ${#backups[@]} backup director$( [[ ${#backups[@]} -eq 1 ]] && echo 'y' || echo 'ies' )."
  fi
fi
