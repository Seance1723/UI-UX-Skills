#!/usr/bin/env python3
"""Validate the UI/UX skill package."""
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    "references/ui-ux-complete-checklist.md",
    "references/ui-ux-frontend-implementation-rules.md",
    "references/wcag-aa-quick-reference.md",
    "references/design-system-playbook.md",
    "references/top-100-brand-website-analysis.md",
    "templates/ui-ux-brief.md",
    "templates/ui-ux-audit-report.md",
    "templates/component-spec.md",
    "templates/design-system-spec.md",
    "templates/top-brand-frontend-spec.md",
]
REQUIRED_PHRASES = [
    "Information Architecture",
    "User Flows",
    "Accessibility",
    "Design Systems",
    "Responsive",
    "Handoff",
    "WCAG",
    "Screen State Checklist",
    "Top-Brand Frontend Method",
    "ui-ux-frontend-implementation-rules.md",
    "top-100-brand-website-analysis.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")

    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter at byte 0")

    match = re.search(r"\n---\s*\n", content[4:])
    if not match:
        fail("SKILL.md frontmatter is not closed")

    end = match.end() + 4
    frontmatter_text = content[4 : match.start() + 4]
    body = content[end:]
    if not body.strip():
        fail("SKILL.md body is empty")

    frontmatter = {}
    for raw_line in frontmatter_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("hermes:"):
            continue
        if ":" in line and not line.startswith("-"):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and not raw_line.startswith("    "):
                frontmatter[key] = value

    for key in ["name", "description", "version", "author", "license", "metadata"]:
        if key not in frontmatter_text:
            fail(f"frontmatter missing {key}")

    name = frontmatter.get("name", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
        fail("name must be lowercase hyphenated and <=64 chars")

    description = frontmatter["description"]
    if not isinstance(description, str) or len(description) > 1024:
        fail("description must be a string <=1024 chars")
    if not description.startswith("Use when"):
        fail('description should start with "Use when"')

    if len(content) > 100_000:
        fail("SKILL.md exceeds 100,000 characters")

    for phrase in REQUIRED_PHRASES:
        if phrase not in content:
            fail(f"SKILL.md missing required phrase: {phrase}")

    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing supporting file: {rel}")
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 200:
            fail(f"supporting file too small or empty: {rel}")

    print("PASS: UI/UX skill package is valid")
    print(f"Root: {ROOT}")
    print(f"Files checked: {1 + len(REQUIRED)}")


if __name__ == "__main__":
    main()
