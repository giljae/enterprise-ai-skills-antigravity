#!/usr/bin/env python3
"""Validate the Enterprise AI Antigravity skill source tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "antigravity" / "enterprise-ai"
REQUIRED_COMMANDS = [
    "scpr",
    "issue-tree",
    "decision-memo",
    "storyline",
    "prioritization",
    "meeting-prep",
    "ai-use-case-scorer",
    "mckinsey-critic",
    "deck-pipeline",
    "data-insights",
    "gamma-deck",
]
REQUIRED_ROOT_FILES = ["SKILL.md", "README.md", "VERSION", "LICENSE"]
REFERENCE_RE = re.compile(r"`((?:references|examples|scripts)/[^`]+)`")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"File is not UTF-8 text: {path}", errors)
        return ""


def validate_frontmatter(path: Path, errors: list[str]) -> None:
    text = read_text(path, errors)
    if not text.startswith("---\n"):
        fail(f"Missing YAML frontmatter: {path}", errors)
        return
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"Unclosed YAML frontmatter: {path}", errors)
        return
    frontmatter = text[4:end]
    for key in ("name:", "version:", "description:", "allowed-tools:"):
        if key not in frontmatter:
            fail(f"Missing `{key}` in frontmatter: {path}", errors)


def validate_references(path: Path, errors: list[str]) -> None:
    text = read_text(path, errors)
    for match in REFERENCE_RE.finditer(text):
        referenced = path.parent / match.group(1)
        if not referenced.exists():
            fail(f"Broken referenced path in {path}: {match.group(1)}", errors)


def validate_scripts(errors: list[str]) -> None:
    expected = [
        SUITE / "data-insights" / "scripts" / "analyze_data.py",
        SUITE / "data-insights" / "scripts" / "requirements.txt",
        SUITE / "gamma-deck" / "scripts" / "gamma_deck_generator.py",
        SUITE / "gamma-deck" / "scripts" / "requirements.txt",
    ]
    for path in expected:
        if not path.exists():
            fail(f"Missing script artifact: {path}", errors)


def main() -> int:
    errors: list[str] = []

    if not SUITE.exists():
        print(f"Missing suite directory: {SUITE}", file=sys.stderr)
        return 1

    for filename in REQUIRED_ROOT_FILES:
        path = SUITE / filename
        if not path.exists():
            fail(f"Missing root file: {path}", errors)

    validate_frontmatter(SUITE / "SKILL.md", errors)
    validate_references(SUITE / "SKILL.md", errors)

    for command in REQUIRED_COMMANDS:
        skill = SUITE / command / "SKILL.md"
        if not skill.exists():
            fail(f"Missing command SKILL.md: {skill}", errors)
            continue
        validate_frontmatter(skill, errors)
        validate_references(skill, errors)

    validate_scripts(errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed: {SUITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
