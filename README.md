# UI/UX Master

[![npm version](https://img.shields.io/npm/v/ui-ux-master?logo=npm&label=npm&color=6366f1)](https://www.npmjs.com/package/ui-ux-master)
[![downloads](https://img.shields.io/npm/dm/ui-ux-master?logo=npm&label=downloads&color=10b981)](https://www.npmjs.com/package/ui-ux-master)
[![License: MIT](https://img.shields.io/npm/l/ui-ux-master?color=f59e0b)](https://github.com/Seance1723/UI-UX-Skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![GitHub stars](https://img.shields.io/github/stars/Seance1723/UI-UX-Skills?style=flat&logo=github)](https://github.com/Seance1723/UI-UX-Skills/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/Seance1723/UI-UX-Skills?logo=github)](https://github.com/Seance1723/UI-UX-Skills/commits/main)

**Turn your AI coding agent into a Senior Product Designer, UX Researcher, and Frontend Lead — in one command.**

One trigger. Every agent. Full design lifecycle from discovery to developer handoff.

```text
/ui-ux-master build a SaaS landing page for my project management tool
```

---

## Install with npm

```bash
# Recommended — project install
npm install --save-dev ui-ux-master
npx ui-ux-master install --project

# No install needed (one-time)
npx ui-ux-master install --project
```

Works with **Claude**, **Windsurf**, **Cursor**, **Codex**, **Gemini**, and any agent that supports instruction files.

---

## Quick Start — Try These

```text
/ui-ux-master audit this dashboard for accessibility and give me fixes
```

```text
/ui-ux-master design a checkout flow for my e-commerce app
```

```text
/ui-ux-master build a landing page for a healthcare startup
```

```text
/ui-ux-master create a full design system for this SaaS product
```

> The skill only activates when you type `/ui-ux-master` — your normal coding workflow is untouched.

---

## What It Does

| Without UI/UX Master | With UI/UX Master |
|---|---|
| Jumps straight to code | Discovery form first — brief, audience, and brand locked before design |
| Generic colors and layout | Industry reasoning engine → instant Design System Block per product type |
| No design system | Portable 9-section schema saved to `.ui-ux-memory.md` per project |
| Ignores accessibility | WCAG 2.2 AA + ARIA patterns audited on every output |
| AI slop output | Anti-slop blacklist + 5-dimensional quality gate before every emit |
| One-size-fits-all style | 20+ named UI styles with complete token overrides |
| Forgets your brand | Design memory persists across all sessions |

---

## What's New

### v1.5.0 — Industry Intelligence Update *(May 2026)*

- **Industry Reasoning Engine** — describe your product, get a complete Design System Block instantly (pattern + style + palette + typography + effects + anti-patterns) for 15+ industries
- **UI Styles Catalog** — 20+ named styles: Glassmorphism, Liquid Glass, Data Brutalism, Aurora Borealis, Cyberpunk, AI-Native, Bento Grid, Soft UI Evolution, Claymorphism, and more — each with full CSS token overrides
- **Architectural Color Scales** — 11-step (50–950) OKLch ramps for every hue family, semantic states, and dark mode mappings
- **16-Framework Tech Stack Guidelines** — React, Next.js, Vue, Nuxt, Angular, Svelte, Astro, Remix, SolidJS, React Native, Flutter, SwiftUI, shadcn/ui, Jetpack Compose, Laravel, HTML+Tailwind
- **Landing Page Patterns** — 12 named conversion patterns (Hero-Centric, Problem-Solution, Social Proof First, Comparison, Product Demo First, and more) with section-by-section structure
- **Chart Type Guide** — 25-type decision tree + dashboard layout rules and anti-patterns
- **Code-Level AI Audit** — 30 error codes (AI001–AI030): Tailwind interpolation bugs, hallucinated utilities, missing a11y, React anti-patterns, invented metrics — each with severity level and line reference
- **MASTER + Page Overrides** — `design-system/MASTER.md` + `pages/[page].md` hierarchy for multi-page consistency

### v1.4.0 — Quality Gates Update

- 6-question discovery form runs before any visual output
- Brand extraction protocol — never guesses colors from a company name
- 5 OKLch visual directions for brandless projects
- 5-dimensional self-critique + P0/P1/P2 quality gates before every emit
- Anti-AI-slop blacklist — purple gradients, generic emojis, invented metrics all forbidden
- Portable 9-section design system schema (DESIGN.md-compatible)

### v1.3.0 — Brand Methods Update

- 10 top-brand design method skill files (Product Cinema, Enterprise Trust Hub, Conversion Simplicity, and more)
- Color Psychology and Branding skill with industry-specific palette prescriptions

---

## Supported Agents

| Agent | Trigger |
|---|---|
| Claude Code | `/ui-ux-master` (native slash command) |
| Windsurf / Cascade | `/ui-ux-master` |
| Cursor | `/ui-ux-master` |
| Codex | `/ui-ux-master` |
| Gemini CLI | `/ui-ux-master` |
| Antigravity | `/ui-ux-master` |
| Any other agent | Copy `agent-templates/universal/` into your instruction file |
| MCP clients | Auto-discovered via `ui-ux-master-mcp` |

---

## MCP Server

```bash
npx -y --package ui-ux-master ui-ux-master-mcp
```

```json
{
  "mcpServers": {
    "ui-ux-master": {
      "command": "npx",
      "args": ["-y", "--package", "ui-ux-master", "ui-ux-master-mcp"]
    }
  }
}
```

---

## CLI Reference

```bash
ui-ux-master install --project                             # install for current project
ui-ux-master install --project --agents claude,windsurf   # specific agents only
ui-ux-master install --project --dry-run                  # preview without writing
ui-ux-master install --global                             # global install
ui-ux-master doctor                                       # check install health
ui-ux-master uninstall --project                          # remove
```

---

## Full Capabilities

<details>
<summary>Expand to see everything</summary>

**Design & Research**
- UX strategy, user goals, jobs-to-be-done
- UX research plans and evidence-confidence scoring
- Information architecture, navigation, taxonomy, search/filter models
- User flows, task flows, journey maps, service blueprints
- Wireframes, layout specs, visual direction, interaction design

**Accessibility**
- WCAG 2.2 AA audits and remediation guidance
- Advanced ARIA patterns: dialogs, tabs, comboboxes, menus, grids, live regions, drag/drop

**Design Systems**
- Token architecture, component specs, governance, usage rules
- Portable 9-section schema saved per project (`.ui-ux-memory.md`)
- MASTER.md + page-level override hierarchy

**Content & Platform**
- UX writing, error copy, empty states, i18n, RTL
- Web, iOS, Android/Material, Windows, kiosk, email, TV

**Specialized Screens**
- SaaS dashboards, data visualization, ecommerce, checkout, onboarding, auth, forms, landing pages

**Ethics & Handoff**
- Dark-pattern detection, privacy, consent, AI transparency, high-risk domain safeguards
- Developer handoff: states, tokens, responsive behavior, analytics events, QA, acceptance criteria

</details>

---

## Package Layout

```
ui-ux-master/
├── SKILL.md                         main orchestration (steps 1–12)
├── references/
│   ├── industry-reasoning-rules.md  15+ industry → instant design system
│   ├── ui-styles-catalog.md         20+ named styles with full token specs
│   ├── color-scale-system.md        11-step OKLch architectural scales
│   ├── tech-stack-guidelines.md     16 frameworks with component patterns
│   ├── landing-page-patterns.md     12 patterns + 25-type chart guide
│   ├── output-quality-gates.md      AI audit codes + 5-dim self-critique
│   ├── design-system-schema.md      9-section schema + MASTER/overrides
│   ├── visual-directions.md         5 OKLch directions for brandless projects
│   ├── design-discovery-protocol.md 6-question intake + brand extraction
│   └── brand-method-*.md            10 top-brand design methods
├── templates/                       briefs, specs, memory template
├── agent-templates/                 Claude, Windsurf, Cursor, Codex, Gemini
├── system-prompts/                  copy into any AI custom-instructions
└── bin/                             CLI + MCP server
```

---

## Validation and Testing

```bash
python scripts/validate_skill.py --release
npm test
npm pack --dry-run
```

Expected output: `PASS: UI/UX skill package is valid`

---

## Limitations

- Guides research — does not replace real user testing
- Assists accessibility review — does not replace AT expert testing for high-risk products
- Flags legal/privacy risks — does not replace legal review
- No live preview or media generation

---

## Competitive Positioning

UI/UX Master combines what every competitor does best into one opt-in, daemon-free, cross-agent skill:

- **Discovery-first** — no visuals until brief is locked (beats generic prompt packs)
- **Industry reasoning engine** — instant Design System Block per product type (matches `ui-ux-pro-max-skill`)
- **11-step OKLch color scales** — architectural palette system (matches `saifyxpro`)
- **Code-level audit AI001–AI030** — catches Tailwind bugs, missing a11y, React anti-patterns (matches `saifyxpro`)
- **16-framework tech stack rules** — component patterns per framework (matches `saifyxpro`)
- **Quality gates** — 5-dimensional self-critique + anti-slop blacklist (inspired by `open-design`)
- **Full lifecycle** — research → IA → UI → accessibility → dev handoff (beats all narrow skills)
- **Project memory** — `.ui-ux-memory.md` persists brand/design across sessions

See `references/competitive-landscape.md` for the full analysis.

---

## Deployment Readiness Checklist

- [ ] `python scripts/validate_skill.py --release` passes
- [ ] `npm test` passes
- [ ] `npm pack --dry-run` contains only intended files
- [ ] `ui-ux-master install --project --dry-run` works
- [ ] No `node_modules`, `.pyc`, secrets, or local paths in package

---

## License

MIT — by Rupak Biswas. Contributions welcome.
