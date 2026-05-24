# UI-UX Skills

One-stop UI/UX master skill package for AI agents. It helps agents design, audit, improve, prototype, specify, and hand off user interfaces from basic to advanced practice.

## What This Package Covers

- UX strategy and product/user understanding.
- UX research methods and evidence quality.
- Information architecture, user flows, journey maps, and service blueprints.
- Wireframes, visual design, interaction design, responsive behavior, and platform guidelines.
- Accessibility from WCAG basics to advanced ARIA/widget patterns.
- Content design, UX writing, localization, and internationalization.
- Design systems, tokens, components, states, governance, and handoff.
- Usability heuristics, audits, usability testing, and quality gates.
- Forms, ecommerce, dashboards, data visualization, conversion, ethics, privacy, and inclusive design.
- Top-brand design inspiration methods without copying trademarks or proprietary layouts.

## Package Structure

- `SKILL.md` — main orchestration skill loaded by agents.
- `references/` — detailed playbooks, checklists, standards, and implementation rules.
- `templates/` — reusable briefs, audit reports, component specs, design-system specs, frontend specs, and UI/UX memory template.
- `scripts/validate_skill.py` — dependency-free validation script.

## Installation

Copy this folder into a Hermes-compatible skill location, for example:

```bash
mkdir -p "$HOME/AppData/Local/hermes/skills/creative/ui-ux-master"
cp -R . "$HOME/AppData/Local/hermes/skills/creative/ui-ux-master/"
```

On another platform, use the appropriate Hermes skills directory and preserve the same folder structure.

## Usage

In a new session, ask the agent to load and use the skill:

```text
Load the ui-ux-master skill and produce a complete UI/UX plan for my SaaS dashboard.
```

For frontend implementation work, the agent should also follow:

- `references/ui-ux-frontend-implementation-rules.md`
- `references/ui-ux-memory-workflow.md`
- `templates/ui-ux-memory.md`

## Validation

Run from this folder:

```bash
python scripts/validate_skill.py
```

Expected result:

```text
PASS: UI/UX skill package is valid
```

For release packaging checks:

```bash
python scripts/validate_skill.py --release
```

Release mode warns or fails on generated artifacts, missing README sections, missing referenced files, and incomplete required headings.

## Deployment Readiness Checklist

- [ ] `python scripts/validate_skill.py` passes.
- [ ] `python scripts/validate_skill.py --release` passes or documented non-release artifacts are intentionally excluded from the deploy package.
- [ ] `SKILL.md` frontmatter is valid and description starts with `Use when`.
- [ ] All referenced files in `SKILL.md` exist.
- [ ] README includes installation, usage, validation, and deployment notes.
- [ ] No `__pycache__`, `.pyc`, temporary files, secrets, or local-only credentials are included in the release package.
- [ ] If graphify outputs are kept in the repo, exclude `graphify-out/cache/` from the deployment bundle unless needed for development.

## Maintenance

- Update references when WCAG, platform guidelines, or design-system conventions change.
- Keep `SKILL.md` as the orchestration layer and move long checklists into `references/`.
- After code or documentation changes, run validation and update the graphify knowledge graph if this repository uses graphify.
- Label top-brand material as pattern inspiration, not live brand audit data.

## Known Limitations

- This skill can guide research planning but cannot replace real users, qualified accessibility testing, legal review, or domain experts in high-risk contexts.
- Brand and competitor websites change over time; verify current claims before citing them as facts.
- AI-generated personas, journeys, and research findings are assumptions unless backed by evidence.

## License

MIT, unless your containing repository specifies otherwise.
