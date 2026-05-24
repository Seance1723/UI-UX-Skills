# UI/UX Master 🎨✨

[![npm version](https://img.shields.io/npm/v/ui-ux-master?logo=npm&label=npm)](https://www.npmjs.com/package/ui-ux-master)
[![npm downloads](https://img.shields.io/npm/dm/ui-ux-master?logo=npm&label=downloads)](https://www.npmjs.com/package/ui-ux-master)
[![License: MIT](https://img.shields.io/npm/l/ui-ux-master)](https://github.com/Seance1723/UI-UX-Skills/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Seance1723/UI-UX-Skills?style=flat&logo=github)](https://github.com/Seance1723/UI-UX-Skills/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/Seance1723/UI-UX-Skills?logo=github)](https://github.com/Seance1723/UI-UX-Skills/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**The ultimate UI/UX skill for AI coding agents.** Turn your AI into a Senior Product Designer, UX Researcher, and Frontend Lead in seconds.

Author: Rupak Biswas.

Use it with a normal prompt plus one trigger:

```text
/ui-ux-master audit this dashboard and give me implementation-ready fixes
```

If `/ui-ux-master` is not present, the installed rules tell agents not to use the skill. That keeps your normal coding workflow clean and makes UI/UX mode explicit.

## Why Use UI/UX Master?

Most AI UI prompts produce pretty screens but miss the hard parts: research assumptions, information architecture, accessibility, responsive states, design-system consistency, platform conventions, localization, ethics, and developer handoff.

UI/UX Master is built to make agents behave like a senior product designer, UX researcher, accessibility reviewer, design-system lead, and frontend handoff partner in one workflow.

## 🚀 Supercharge Your AI Workflow

AI agents are great at writing code, but they often struggle with **Information Architecture**, **Accessibility (WCAG)**, and **Design Systems**. `ui-ux-master` bridges this gap. 

By installing this tool, you instantly give **Claude**, **Cursor**, **Windsurf**, **Codex**, **Gemini**, **Antigravity**, and universal/custom-instruction agents the ability to:
- 🧠 **Think like a designer:** Understand user flows and journey maps before coding.
- ♿ **Audit for accessibility:** Automatically check for WCAG 2.2 AA compliance and ARIA patterns.
- 🧩 **Enforce design systems:** Keep your brand colors, typography, and spacing consistent.

## What Makes It Different

| Common open-source prompt/skill | UI/UX Master |
|---|---|
| Focuses on visual polish only | Covers research, UX strategy, IA, flows, UI, accessibility, content, metrics, and handoff |
| Always-on rules that interfere with normal coding | Opt-in `/ui-ux-master` trigger only |
| One agent or editor only | Cross-agent templates for Claude, Codex, Windsurf, Antigravity, Gemini, Cursor, and universal agents |
| Generic design advice | Concrete templates, checklists, quality gates, and implementation rules |
| No persistent design memory | Project `.ui-ux-memory.md` workflow keeps brand/design decisions consistent |
| Weak accessibility coverage | WCAG 2.2 AA plus advanced ARIA/widget patterns and test matrix |
| No deployment validation | Release validator, npm package metadata, tests, and deployment zip builder |
| No product-risk coverage | Ethics, privacy, dark-pattern, high-risk domain, AI-interface, and inclusive-design checks |
| Hidden from AI tooling | Ships `llms.txt`, machine-readable manifest, system prompt add-ons, and a local MCP server for automatic discovery |

## AI Discoverability

UI/UX Master is now designed for both humans and AI systems to discover:

- `llms.txt` gives agents a concise map of the package.
- `ai-discovery/ui-ux-master.manifest.json` provides a machine-readable manifest.
- `system-prompts/` contains full, compact, and MCP-focused system prompt add-ons.
- `ui-ux-master-mcp` exposes the package through a local MCP server with tools, resources, and prompts.
- Project installs copy these discovery assets into `.ui-ux-master/` so no-save `npx` installs remain usable after the npm cache disappears.

## Capabilities

UI/UX Master can help agents produce:

- Product UX strategy and user goals
- UX research plans, evidence confidence, and research synthesis
- Information architecture, navigation, taxonomy, and search/filter models
- User flows, task flows, journey maps, and service blueprints
- Wireframes, layout specs, visual direction, and interaction design
- Accessibility audits and WCAG 2.2 AA remediation guidance
- Advanced component accessibility patterns for dialogs, tabs, comboboxes, menus, grids, live regions, and drag/drop alternatives
- Design systems, tokens, component specs, governance, and usage rules
- Content design, UX writing, error copy, empty states, localization, RTL, and i18n checks
- Platform-specific guidance for web, iOS, Android/Material, Windows/desktop, kiosk, email, TV, and universal agents
- SaaS dashboards, data visualization, tables, alerts, ecommerce, checkout, onboarding, settings, auth, forms, and landing pages
- Ethical UX, privacy, consent, dark-pattern detection, AI transparency, and high-risk domain safeguards
- Developer handoff with states, tokens, responsive behavior, analytics events, QA, and acceptance criteria

## Install with npm

Global install:

```bash
npm install -g ui-ux-master
ui-ux-master install --global
```

Project-local install, recommended:

```bash
npm install --save-dev ui-ux-master
npx ui-ux-master install --project
```

No-save project install (copies reusable skill files into `.ui-ux-master/` so agents can still read the source after npx exits):

```bash
npx ui-ux-master install --project
```

Install only selected agents:

```bash
npx ui-ux-master install --project --agents claude,codex,windsurf,gemini,cursor
```

Dry run:

```bash
npx ui-ux-master install --project --dry-run
```

## Package

| Channel | Package | Purpose |
|---|---|---|
| npmjs | [`ui-ux-master`](https://www.npmjs.com/package/ui-ux-master) | Primary public package for normal installs and `npx` usage |
| GitHub | [`Seance1723/UI-UX-Skills`](https://github.com/Seance1723/UI-UX-Skills) | Source, issues, releases, workflows, and open-source collaboration |
| GitHub Packages | Optional scoped mirror | Use only if you want the repository Packages section to show a package |

The canonical npm package is intentionally unscoped as `ui-ux-master`. Keep that name in `package.json` for normal npmjs publishing. GitHub Packages requires npm packages to be scoped, so the release workflow temporarily changes the package name to `@seance1723/ui-ux-master` only inside the GitHub Packages publish job. The source package remains `ui-ux-master`.

Install from npmjs:

```bash
npm install ui-ux-master
```

Install the optional GitHub Packages mirror:

```bash
npm install @seance1723/ui-ux-master
```

GitHub Packages often requires authentication even for installs. If npm cannot access the scoped package, configure a token with `read:packages` access:

```ini
@seance1723:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NODE_AUTH_TOKEN}
```

Publishing the scoped mirror to GitHub Packages is what makes the package appear in the repository's Packages section.

Package entrypoints:

- `ui-ux-master` - CLI installer and project integration tool.
- `ui-ux-master-mcp` - local MCP server for tools, resources, and prompts.
- `import { assets, bins, trigger } from "ui-ux-master"` - lightweight ESM metadata API.
- `require("ui-ux-master")` - CommonJS metadata API.

Package metadata is connected to GitHub through `repository`, `homepage`, `bugs`, license, funding, exports, engines, and npm provenance-ready publish settings in `package.json`.

## Supported Agents

| Agent | Install target | Trigger |
|---|---|---|
| Claude Code | `.claude/commands/ui-ux-master.md` | native `/ui-ux-master` command |
| Codex | `AGENTS.md` marked section | type `/ui-ux-master` |
| Windsurf/Cascade | `.windsurf/rules/ui-ux-master.md` and `.windsurfrules` fallback | type `/ui-ux-master` |
| Antigravity | `AGENTS.md` plus `.antigravity/rules/ui-ux-master.md` fallback | type `/ui-ux-master` |
| Gemini CLI | `GEMINI.md` marked section | type `/ui-ux-master` |
| Cursor | `.cursor/rules/ui-ux-master.mdc` | type `/ui-ux-master` |
| Other agents | `agent-templates/universal/ui-ux-master-trigger.md` | copy trigger into instruction file |
| MCP clients | `ui-ux-master-mcp` | discover tools/resources/prompts automatically |

See `docs/slash-command-compatibility.md` for details.

## System Prompt Add-ons

Copy one of these into any AI custom-instructions field when the agent does not support project rules:

- `system-prompts/ui-ux-master-system-add-on.md` — full add-on.
- `system-prompts/ui-ux-master-compact.md` — compact add-on.
- `system-prompts/ui-ux-master-mcp-add-on.md` — MCP-focused add-on.

## MCP Server

Run the local MCP server:

```bash
ui-ux-master-mcp
# or without global install
npx -y --package ui-ux-master ui-ux-master-mcp
```

MCP client config:

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

See `docs/mcp-server.md` for tools, resources, prompts, and Hermes config.

## Usage Examples

```text
/ui-ux-master redesign this SaaS onboarding flow for faster activation and create dev handoff specs
```

```text
/ui-ux-master audit the checkout flow for accessibility, trust, conversion, and mobile UX
```

```text
/ui-ux-master create a design system starter for this app using the existing components and tokens
```

```text
/ui-ux-master inspect this dashboard and improve hierarchy, data visualization, empty states, and responsive behavior
```

```text
/ui-ux-master turn this rough product idea into IA, user flows, wireframes, content, metrics, and implementation tasks
```

## CLI Commands

```bash
ui-ux-master install --project
ui-ux-master install --global
ui-ux-master install --project --agents claude,codex,windsurf,antigravity,gemini,cursor
ui-ux-master install --project --dry-run
ui-ux-master doctor
ui-ux-master where
ui-ux-master mcp
ui-ux-master-mcp
ui-ux-master uninstall --project
```

## Package Structure

- `SKILL.md` — main orchestration skill.
- `index.mjs`, `index.cjs`, `index.d.ts` — ESM, CommonJS, and TypeScript metadata entrypoints.
- `references/` — advanced playbooks and standards-aligned checklists.
- `templates/` — briefs, audits, component specs, design-system specs, and project UI/UX memory template.
- `agent-templates/` — Claude, Codex, Windsurf, Antigravity, Gemini, Cursor, and universal `/ui-ux-master` activation rules.
- `docs/` — cross-agent slash-command compatibility docs and MCP server docs.
- `system-prompts/` — full, compact, and MCP-focused system prompt add-ons.
- `ai-discovery/` — machine-readable discovery manifest.
- `llms.txt` — AI-readable package map.
- `bin/ui-ux-master.mjs` — npm CLI installer.
- `bin/ui-ux-master-mcp.mjs` — local MCP server.
- `scripts/validate_skill.py` — dependency-free release validator.
- `scripts/build_deployment_zip.py` — clean deployment zip builder.
- `tests/` — npm installer and package smoke tests.

## GitHub Repository Setup

Recommended About section:

- Description: `Opt-in UI/UX master skill, CLI, and MCP server for AI coding agents. Accessibility, design systems, UX research, and frontend handoff in one workflow.`
- Website: `https://www.npmjs.com/package/ui-ux-master`
- Enable releases and issues. Enable discussions when you are ready to support community questions.

Recommended GitHub topics:

`ai-agent`, `ai-coding`, `ui-ux`, `ux-research`, `product-design`, `design-system`, `accessibility`, `wcag`, `mcp`, `model-context-protocol`, `claude-code`, `codex`, `windsurf`, `cursor`, `gemini-cli`, `npm-package`, `cli`, `prompt-engineering`, `frontend`, `llms-txt`

For publishing and registry details, see `docs/package-publishing.md`.

## Validation and Testing

Run from this folder:

```bash
python scripts/validate_skill.py --release
npm test
npm pack --dry-run
```

Build a clean deployment zip:

```bash
python scripts/build_deployment_zip.py
```

Expected validation result:

```text
PASS: UI/UX skill package is valid
Release mode: PASS
```

## Competitive Positioning

UI/UX Master is designed to outperform narrow UI prompt packs and simple design rules by combining:

1. Opt-in activation: no pollution of normal coding prompts.
2. Cross-agent portability: one package for Claude, Codex, Windsurf, Antigravity, Gemini, Cursor, and generic agents.
3. Full lifecycle coverage: discovery to deployment handoff.
4. Standards alignment: WCAG, WAI-ARIA patterns, GOV.UK, NN/g, Material, Apple HIG, Microsoft, Baymard-style ecommerce practice, ISO human-centered design concepts.
5. Project memory: durable brand/design consistency via `.ui-ux-memory.md`.
6. Release engineering: npm packaging, CLI installer, validation, tests, and deployment zip.
7. Advanced risk coverage: ethics, privacy, dark patterns, localization, platform conventions, high-risk domains, and AI UX transparency.
8. AI discoverability: `llms.txt`, manifest, system prompt add-ons, and local MCP server.

## Deployment Readiness Checklist

- [ ] `python scripts/validate_skill.py --release` passes.
- [ ] `npm test` passes.
- [ ] `npm pack --dry-run` contains only intended files.
- [ ] `ui-ux-master install --project --dry-run` works.
- [ ] Agent templates contain `/ui-ux-master` and do not include local absolute paths.
- [ ] System prompt add-ons and MCP docs are included and mention `/ui-ux-master`.
- [ ] MCP smoke test returns `tools/list` and `resources/list` successfully.
- [ ] No `node_modules`, `__pycache__`, `.pyc`, graphify cache, coverage, logs, secrets, or local credentials are included.

## Known Limitations

- It guides research planning but does not replace real users.
- It helps accessibility review but does not replace expert assistive-technology testing for high-risk products.
- It flags legal/privacy/health/finance risks but does not replace legal or domain-expert review.
- Brand and competitor sites change; verify live claims before citing them as facts.
- Agents without native slash commands use `/ui-ux-master` as a text trigger through installed instruction files.

## License

MIT.
