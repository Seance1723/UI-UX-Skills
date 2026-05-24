#!/usr/bin/env python3
"""Validate the UI/UX skill package.

Dependency-free by design so the package can be checked on a fresh machine.
Use --release for stricter deployment packaging checks.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"

REQUIRED = [
    "README.md",
    "references/ui-ux-complete-checklist.md",
    "references/ui-ux-frontend-implementation-rules.md",
    "references/ui-ux-memory-workflow.md",
    "references/wcag-aa-quick-reference.md",
    "references/design-system-playbook.md",
    "references/top-100-brand-website-analysis.md",
    "references/ux-research-methods.md",
    "references/usability-heuristics.md",
    "references/platform-guidelines.md",
    "references/content-design-and-i18n.md",
    "references/ux-measurement-quality-gates.md",
    "references/ethical-inclusive-design.md",
    "references/service-design-journey-mapping.md",
    "references/data-visualization-dashboard-ux.md",
    "references/accessibility-advanced-patterns.md",
    "references/ui-ux-curriculum-and-standards.md",
    "templates/ui-ux-brief.md",
    "templates/ui-ux-memory.md",
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
    "UI/UX memory",
    "research",
    "heuristic",
    "platform",
    "content design",
    "Internationalization",
    "Measurement and Quality Gates",
    "Ethics",
    "privacy",
]

REQUIRED_HEADINGS = {
    "README.md": ["## Installation", "## Usage", "## Validation", "## Deployment Readiness Checklist"],
    "references/ux-research-methods.md": ["## Research Decision Tree", "## Research Plan Template", "## Evidence Confidence Levels"],
    "references/usability-heuristics.md": ["## Nielsen's 10 Usability Heuristics", "## Severity Rating"],
    "references/platform-guidelines.md": ["## Web App", "## iOS / Apple Platforms", "## Android / Material", "## Cross-Platform Rule"],
    "references/content-design-and-i18n.md": ["## Content Design Principles", "## Internationalization Checklist"],
    "references/ux-measurement-quality-gates.md": ["## Metric Selection", "## Quality Gate Template"],
    "references/ethical-inclusive-design.md": ["## Dark Pattern Checks", "## Privacy UX", "## Inclusive Design"],
    "references/service-design-journey-mapping.md": ["## Journey Map Elements", "## Service Blueprint Elements"],
    "references/data-visualization-dashboard-ux.md": ["## Dashboard Principles", "## Chart Selection", "## Tables and Data Grids"],
    "references/accessibility-advanced-patterns.md": ["## Complex Widget Checklist", "## Testing Matrix"],
    "references/ui-ux-curriculum-and-standards.md": ["## Beginner Foundations", "## Intermediate Practice", "## Advanced Practice"],
    "templates/ui-ux-brief.md": ["## Research and Evidence Plan", "## Constraints", "## Deliverables Needed"],
    "templates/ui-ux-audit-report.md": ["## Heuristic Findings", "## Measured Evidence and Quality Gates"],
    "templates/component-spec.md": ["## Acceptance Criteria and Test Matrix"],
    "templates/design-system-spec.md": ["## Governance"],
    "templates/top-brand-frontend-spec.md": ["## 11. Quality Gates", "## 12. Do Not Copy"],
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter at byte 0")
    end_marker = content.find("\n---\n", 4)
    if end_marker == -1:
        fail("SKILL.md frontmatter is not closed")
    frontmatter_text = content[4:end_marker]
    body = content[end_marker + 5 :]
    if not body.strip():
        fail("SKILL.md body is empty")

    frontmatter: dict[str, str] = {}
    for raw_line in frontmatter_text.splitlines():
        if not raw_line or raw_line.startswith(" ") or raw_line.lstrip().startswith("#"):
            continue
        if ":" in raw_line:
            key, value = raw_line.split(":", 1)
            frontmatter[key.strip()] = value.strip().strip('"').strip("'")
    return frontmatter, body


def check_required_files() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing supporting file: {rel}")
        text = path.read_text(encoding="utf-8")
        min_len = 500 if rel.endswith(".md") else 200
        if len(text.strip()) < min_len:
            fail(f"supporting file too small or empty: {rel}")


def check_required_headings() -> None:
    for rel, headings in REQUIRED_HEADINGS.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                fail(f"{rel} missing heading: {heading}")


def check_skill_frontmatter_and_body() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")
    content = SKILL.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    for key in ["name", "description", "version", "author", "license", "metadata"]:
        if key not in content.split("---", 2)[1]:
            fail(f"frontmatter missing {key}")

    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
        fail("name must be lowercase hyphenated and <=64 chars")

    description = fm.get("description", "")
    if len(description) > 1024:
        fail("description must be <=1024 chars")
    if not description.startswith("Use when"):
        fail('description should start with "Use when"')

    if len(content) > 100_000:
        fail("SKILL.md exceeds 100,000 characters")
    if len(content) > 45_000:
        warn("SKILL.md is getting large; keep detailed material in references/")

    lower_body = body.lower()
    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in lower_body:
            fail(f"SKILL.md missing required phrase: {phrase}")


def check_referenced_files_exist() -> None:
    content = SKILL.read_text(encoding="utf-8")
    refs = sorted(set(re.findall(r"`((?:references|templates)/[^`]+?\.md|README\.md)`", content)))
    for rel in refs:
        if not (ROOT / rel).exists():
            fail(f"SKILL.md references missing file: {rel}")


def check_markdown_links() -> None:
    # Check local markdown links only. External links are intentionally not fetched.
    for path in [ROOT / rel for rel in REQUIRED if rel.endswith(".md")]:
        text = path.read_text(encoding="utf-8")
        for match in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if match.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (path.parent / match.split("#", 1)[0]).resolve()
            if not target.exists():
                fail(f"broken local markdown link in {path.relative_to(ROOT)}: {match}")


def check_release_artifacts(strict: bool) -> None:
    bad_patterns = ["**/__pycache__", "**/*.pyc", "**/.DS_Store", "**/Thumbs.db", "graphify-out/cache"]
    found: list[str] = []
    for pattern in bad_patterns:
        for path in ROOT.glob(pattern):
            found.append(str(path.relative_to(ROOT)))
    if found:
        message = "release artifacts found: " + ", ".join(sorted(found)[:12])
        if strict:
            fail(message)
        warn(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true", help="run stricter deployment packaging checks")
    args = parser.parse_args()

    check_skill_frontmatter_and_body()
    check_required_files()
    check_required_headings()
    check_referenced_files_exist()
    check_markdown_links()
    check_release_artifacts(strict=args.release)

    print("PASS: UI/UX skill package is valid")
    print(f"Root: {ROOT}")
    print(f"Files checked: {1 + len(REQUIRED)}")
    if args.release:
        print("Release mode: PASS")


if __name__ == "__main__":
    main()
