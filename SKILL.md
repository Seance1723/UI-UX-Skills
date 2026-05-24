---
name: ui-ux-master
description: "Use when an agent must design, audit, improve, prototype, specify, or hand off any UI/UX work end-to-end. Provides one-stop UX strategy, research, IA, flows, wireframes, visual design, design systems, accessibility, usability testing, conversion, and engineering handoff workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ui, ux, product-design, accessibility, design-system, prototyping, audit, frontend]
    related_skills: [popular-web-designs, sketch, claude-design, design-md, excalidraw, humanizer, writing-plans]
---

# UI/UX Master Skill

## Overview

This is a one-stop UI/UX skill for agents. Use it whenever the user asks for anything related to user experience, interface design, product design, design systems, wireframes, prototypes, frontend polish, accessibility, conversion, usability, or design critique.

The job is not only to make screens look good. The job is to solve the user's goal with a usable, accessible, coherent, implementable interface. Always connect design choices to user needs, product goals, content, system constraints, and measurable outcomes.

## Core Operating Rule

Do not jump directly to visuals. Work in this order unless the user explicitly asks for a narrow task:

1. Check for existing UI/UX memory and branding first: `.ui-ux-memory.md`, design tokens, CSS variables, theme files, existing components, fonts, color scheme, and representative screens.
2. If memory exists, follow it as the design baseline. If no memory exists, create one for the application using `templates/ui-ux-memory.md` after inspecting existing branding or asking minimum high-value questions for a fresh project.
3. Understand the product, users, goal, platform, constraints, and success metric.
4. Define the UX model: audience, jobs-to-be-done, journeys, information architecture, flows, states, and content.
5. Select an appropriate top-brand design method when frontend polish is requested: Product Cinema, Utility Command Center, Editorial Brand World, Enterprise Trust Hub, Card-Based Discovery, Conversion Simplicity, Ecosystem Bundling, Premium Restraint, Playful Familiarity, or Technical Authority.
6. Design the interface by extending the existing memory/brand baseline unless the user explicitly asks for a redesign or specific visual modification.
7. Validate: consistency with memory, heuristics, WCAG, usability risks, edge cases, technical feasibility, and brand-fit.
8. Update the application UI/UX memory with durable design decisions before handoff.
9. Hand off: exact specs, tokens, component behavior, copy, states, QA checklist, implementation notes.

## When to Use

Use this skill for:

- New app, website, dashboard, landing page, SaaS, mobile, admin, ecommerce, onboarding, forms, checkout, settings, profile, search, data tables, empty states, error states, auth, or any other UI.
- Redesigning, modernizing, polishing, or improving an existing screen.
- Creating UX plans, design briefs, IA, user flows, wireframes, prototypes, mockups, design systems, or style guides.
- Reviewing UI/UX quality, accessibility, conversion, usability, responsiveness, or handoff readiness.
- Turning vague product ideas into design requirements.
- Translating Figma/design screenshots into implementation-ready frontend instructions.
- Giving agents a repeatable UI/UX process across all projects.

Do not use this skill for pure backend work with no user-facing behavior, unless API decisions affect UX states, latency, data shape, validation, or error handling.

## Required Agent Behavior

### Ask Only High-Value Questions

If the user gave enough context, proceed with assumptions and label them. Ask questions only when missing context would materially change the design.

High-value questions:

- Who is the primary user and what job are they trying to complete?
- What platform: web, mobile, desktop, kiosk, email, dashboard, embedded widget?
- What is the primary success metric: activation, conversion, retention, task completion, speed, trust, comprehension?
- Is there an existing brand, design system, tech stack, or accessibility requirement?
- Are there competitor or reference products the user likes/dislikes?

### Always Produce Useful Output

For design tasks, include concrete artifacts, not just advice:

- Design direction and rationale.
- IA/site map or screen inventory.
- User flow or task flow.
- Layout/wireframe description.
- Component list and states.
- Copy recommendations.
- Responsive behavior.
- Accessibility requirements.
- Implementation/handoff checklist.
- Testing and QA checklist.

### Prefer Specifics Over Taste

Avoid vague language like "make it modern" or "improve UX" unless followed by exact changes. Say what to change, where, and why.

Bad: "Make the hero cleaner."
Good: "Reduce hero to one H1, one 18px supporting sentence, one primary CTA, one secondary proof link; move feature bullets below fold to reduce decision load."

## Universal UI/UX Workflow

### Phase 1: Product and User Understanding

Capture:

- Product category and promise.
- Primary user segments.
- User jobs-to-be-done.
- Business goals.
- Platform and context of use.
- Constraints: time, tech stack, brand, compliance, device, content, localization.
- Known data inputs/outputs.
- Existing analytics or user feedback if available.

Deliverable: short design brief.

### Phase 2: UX Strategy

Define:

- Primary and secondary use cases.
- Main user journey.
- Decision points and friction points.
- Prioritized screens.
- Success metrics and guardrail metrics.
- Risks and assumptions.

Deliverable: UX strategy summary.

### Phase 3: Information Architecture

Create:

- Navigation model.
- Page/screen hierarchy.
- Content grouping.
- Labels and terminology.
- Search/filter/sort model where applicable.
- Permission/role visibility if applicable.

Principles:

- Use user vocabulary, not internal system vocabulary.
- Put the most common task in the shortest path.
- Progressive disclosure beats dense first screens.
- Group by user intent, not database schema.

Deliverable: IA map or screen inventory.

### Phase 4: User Flows

For each key task, define:

- Entry point.
- Required user decision.
- System response.
- Success path.
- Empty/error/loading/permission states.
- Recovery path.
- Exit/next best action.

Deliverable: flow steps or diagram.

### Phase 5: Wireframes and Layout

Design screen structure:

- Page goal.
- Primary action.
- Secondary actions.
- Visual hierarchy.
- Grid and spacing.
- Content modules.
- Component placement.
- Above-the-fold priorities.

For every screen, specify:

- Header/navigation.
- Main content region.
- Sidebars/panels if any.
- Footer or persistent actions.
- Responsive collapse behavior.

Deliverable: wireframe description or quick HTML/ASCII/diagram when useful.

### Phase 6: Visual Design

Define visual language:

- Brand personality: e.g. calm, premium, playful, technical, enterprise, editorial.
- Color palette and semantic color roles.
- Typography scale.
- Spacing scale.
- Radius, shadows, borders, elevation.
- Iconography and illustration style.
- Motion style.
- Density: compact, comfortable, spacious.

Rules:

- Use color semantically, not decoratively only.
- One dominant visual idea per screen.
- Establish hierarchy with size, weight, spacing, contrast, and grouping.
- Maintain consistent component behavior across screens.

Deliverable: style direction and design tokens.

### Phase 7: Interaction Design

Specify:

- Hover, focus, active, selected, disabled states.
- Loading and skeleton states.
- Empty states.
- Error and validation behavior.
- Confirmation patterns.
- Undo vs destructive confirmation.
- Keyboard support.
- Touch target sizes.
- Motion duration/easing.
- Drag/drop, pagination, infinite scroll, modals, drawers, popovers, tabs, accordions behavior.

Deliverable: interaction spec.

### Phase 8: Accessibility and Inclusive Design

Minimum standard: WCAG 2.2 AA unless user requests stricter.

Check:

- Semantic structure and headings.
- Keyboard navigation and focus order.
- Visible focus indicators.
- Color contrast.
- Text resizing/reflow.
- Touch target sizes.
- Form labels and error messages.
- ARIA only when semantic HTML is insufficient.
- Screen reader names/roles/states.
- Reduced motion.
- Language and reading level.
- Non-color indicators.

Deliverable: accessibility checklist and fixes.

### Phase 9: Content Design and Microcopy

For every screen, consider:

- Clear H1 that matches user intent.
- CTA labels that say what happens next.
- Helpful empty states.
- Recovery-focused error messages.
- Field labels and helper text.
- Confirmation copy.
- Tooltip necessity; avoid hiding critical information in tooltips.
- Tone consistency.

Copy principles:

- Be specific, human, and action-oriented.
- Avoid blame: "We couldn't save changes" instead of "Invalid input".
- Put the fix in the message.
- Use verbs for actions.

Deliverable: suggested copy blocks.

### Phase 10: Prototype and Handoff

Produce implementation-ready handoff:

- Screen list.
- Component inventory.
- Token values.
- Layout specs.
- Responsive rules.
- State matrix.
- Accessibility notes.
- Data requirements.
- Analytics events.
- QA checklist.
- Out-of-scope items.

Deliverable: handoff spec developers can implement without guessing.

## Design Specialties Covered

### Product UX

Use for product structure, onboarding, activation, dashboards, retention loops, notification strategy, settings, permissions, collaboration, lifecycle emails, and feature discovery.

Key questions:

- What is the user's first successful moment?
- What must they understand before they can act?
- What can be deferred until later?
- What feedback confirms progress?
- What state makes users trust the system?

### SaaS and Dashboard UX

Must include:

- Role-based navigation.
- Overview with clear hierarchy: key metrics, alerts, recent activity, next actions.
- Data table behavior: sorting, filtering, search, bulk actions, column management, pagination, empty/error/loading states.
- Chart clarity: title, timeframe, units, legends, annotations, comparison, no misleading axes.
- Drill-down paths.
- Export/share behavior.

### Landing Page and Conversion UX

Must include:

- One clear promise above the fold.
- Primary CTA repeated at logical points.
- Social proof near claims.
- Objection handling.
- Feature-to-benefit translation.
- Pricing clarity if applicable.
- Trust signals.
- FAQ for high-friction questions.
- Performance and mobile-first layout.

### Ecommerce UX

Must include:

- Product discovery: categories, search, filters, sort.
- Product detail: imagery, price, variants, availability, delivery, returns, reviews, trust.
- Cart: editable quantities, transparent costs, saved state.
- Checkout: guest checkout, progress, validation, payment trust, error recovery.
- Post-purchase confirmation and tracking.

### Forms UX

Must include:

- Ask only necessary fields.
- Group fields logically.
- Label every field.
- Use inline validation after user input, not before.
- Preserve entered data on errors.
- Explain why sensitive data is needed.
- Provide input masks/examples for formatted data.
- Make submit state and errors obvious.

### Mobile UX

Must include:

- Thumb-friendly primary actions.
- 44x44 px minimum touch targets.
- Avoid hover-only interactions.
- Handle keyboard viewport changes.
- Reduce dense tables into cards or priority columns.
- Use native patterns where appropriate.
- Offline/poor network states if relevant.

### Design Systems

Must include:

- Foundations: color, typography, spacing, radius, elevation, iconography, motion.
- Components: buttons, inputs, selects, checkboxes, radios, switches, tabs, modals, drawers, cards, tables, alerts, toasts, tooltips, navigation, breadcrumbs, pagination.
- Component anatomy.
- Variants and sizes.
- State matrix.
- Accessibility rules.
- Usage guidelines and anti-patterns.
- Token naming and semantic roles.

### Top-Brand Frontend Method

When the user asks for a frontend that looks polished, premium, world-class, or similar to top brands, use `references/top-100-brand-website-analysis.md` before designing.

Process:

1. Identify the product category and user task.
2. Pick one primary method and one or two supporting methods:
   - Product Cinema for premium product reveals.
   - Utility Command Center for task-heavy ecommerce, booking, logistics, dashboards.
   - Editorial Brand World for fashion, sports, beverage, entertainment, luxury campaigns.
   - Enterprise Trust Hub for B2B, finance, healthcare, infrastructure, industrial.
   - Card-Based Discovery for marketplaces, media, travel, catalogs, content libraries.
   - Conversion Simplicity for signup, trial, app download, subscription, fintech flows.
   - Ecosystem Bundling for multi-product suites.
   - Premium Restraint for luxury, high-end finance, premium services.
   - Playful Familiarity for food, toys, family, consumer brands.
   - Technical Authority for AI, developer tools, semiconductors, infrastructure.
3. Translate the selected methods into original tokens, layout rules, components, states, and copy.
4. Never copy a brand exactly unless the user owns that brand. Avoid logos, proprietary images, exact trademark color combinations, and pixel-for-pixel layouts.
5. Preserve accessibility and usability even when using cinematic, luxury, or experimental layouts.

Deliverable additions:

- Brand-inspiration blend.
- Selected method rationale.
- Layout archetype.
- Token direction.
- Component behavior.
- Accessibility safeguards.
- Anti-copy/IP safety note.

### Frontend Implementation UX

When implementing UI, first load and follow `references/ui-ux-frontend-implementation-rules.md`. Treat it as the non-negotiable frontend implementation checklist.

Before coding, check project dependencies first. Do not assume Tailwind, shadcn, Material UI, Radix, Framer Motion, Bootstrap, or any other library exists. Use existing component conventions whenever possible.

Implementation rules:

- Inspect existing stack, components, routes, styles, tokens, and similar screens before editing.
- Reuse existing components before creating new ones.
- Preserve routing, state management, data fetching, and styling conventions.
- Use semantic HTML.
- Avoid hardcoded magic values when a token system exists.
- Build all states, not only the happy path.
- Implement loading, empty, error, success, disabled, permission, hover, focus, active, and responsive states.
- Test keyboard, focus, screen-reader names, contrast, mobile layout, console errors, and build/lint checks when available.
- Do not mark frontend work complete until the QA checklist in `references/ui-ux-frontend-implementation-rules.md` passes or any remaining gaps are explicitly reported.

## UI/UX Audit Framework

When auditing an existing UI, score each area 1-5 and provide fixes:

1. Clarity: Can users immediately understand what this is and what to do?
2. Hierarchy: Is the most important content/action visually dominant?
3. Flow: Is the task path short, predictable, and recoverable?
4. Content: Is copy specific, useful, and human?
5. Accessibility: Does it meet WCAG AA basics?
6. Consistency: Are components, spacing, terminology, and states consistent?
7. Responsiveness: Does it work well across viewport sizes?
8. Feedback: Are loading, success, error, empty, and disabled states clear?
9. Trust: Are claims, permissions, costs, risks, and system status transparent?
10. Performance perception: Does the UI feel fast and stable?
11. Conversion/task success: Does it reduce friction toward the main goal?
12. Implementation readiness: Can developers build it from the spec?

Output format:

- Executive summary.
- Severity-ranked findings.
- Quick wins.
- Detailed recommendations.
- Accessibility fixes.
- Revised screen structure or copy.
- QA checklist.

## Screen State Checklist

Every meaningful screen/component should define:

- Default.
- Loading.
- Skeleton if loading > 500ms.
- Empty.
- Error.
- Partial data.
- Permission denied.
- Offline/network failure if relevant.
- Disabled.
- Hover.
- Focus.
- Active/pressed.
- Selected/current.
- Validation success/error/warning.
- Success confirmation.
- Undo/recovery.

## Responsive Breakpoints Guidance

Use the project's existing breakpoints if present. If none exist, use:

- Small mobile: 320-374 px.
- Mobile: 375-767 px.
- Tablet: 768-1023 px.
- Desktop: 1024-1439 px.
- Wide: 1440+ px.

Responsive decisions:

- What reflows?
- What collapses?
- What becomes a drawer?
- What becomes horizontally scrollable only if unavoidable?
- What content is prioritized or hidden?
- How do sticky/fixed elements behave?

## Design Token Starter Set

Use semantic tokens, not raw color names in component specs.

Color roles:

- background, surface, surface-raised, surface-muted.
- text-primary, text-secondary, text-muted, text-inverse.
- border, border-strong, focus-ring.
- primary, primary-hover, primary-active, primary-contrast.
- secondary, secondary-hover, secondary-contrast.
- success, warning, danger, info and their background/border/text roles.

Typography roles:

- display, h1, h2, h3, body, body-sm, caption, label, code.

Spacing scale:

- 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80.

Radius:

- none, sm, md, lg, xl, full.

Elevation:

- none, sm, md, lg, overlay.

Motion:

- fast 120ms, base 180ms, slow 240ms.
- easing: standard, enter, exit.

## Handoff Output Template

When asked to produce a final UI/UX spec, use this structure:

1. Goal and assumptions.
2. Users and jobs-to-be-done.
3. UX strategy.
4. Information architecture.
5. Key flows.
6. Screen-by-screen specification.
7. Components and states.
8. Visual direction, top-brand method blend, and tokens.
9. Content and microcopy.
10. Accessibility requirements.
11. Responsive behavior.
12. Analytics events.
13. Developer implementation notes.
14. QA/testing checklist.
15. Open questions and risks.
16. Anti-copy/IP safety notes when inspired by real brands.

## Quality Bar

A UI/UX answer is complete only when it handles:

- User goal.
- Business goal.
- Main flow.
- Edge cases.
- Error/loading/empty states.
- Accessibility.
- Responsiveness.
- Content/microcopy.
- Visual consistency.
- Implementation feasibility.
- Verification.

## Common Pitfalls

1. Starting with colors before solving the flow.
2. Designing only the happy path.
3. Ignoring empty, error, loading, and permission states.
4. Hiding critical actions behind icons without labels.
5. Using low-contrast text or color-only status indicators.
6. Creating new components when the project already has a component system.
7. Writing generic copy that does not tell users what happened or what to do next.
8. Overloading dashboards with metrics but no next action.
9. Making desktop-first layouts that collapse poorly on mobile.
10. Treating accessibility as a final pass instead of a design constraint.
11. Forgetting keyboard users.
12. Overusing modals, carousels, hover-only controls, and vague tooltips.
13. Shipping a mockup without developer-ready states and specs.
14. Choosing trendy visuals that conflict with the product's trust needs.
15. Confusing user personas with stereotypes; focus on tasks, context, and constraints.

## Verification Checklist

Before finalizing UI/UX work, verify:

- [ ] The primary user goal is explicit.
- [ ] The main CTA and next action are obvious.
- [ ] Screen hierarchy supports the main task.
- [ ] Navigation labels match user language.
- [ ] Every interactive element has states.
- [ ] Loading, empty, error, and success states are specified.
- [ ] Forms have labels, validation, helper text, and recovery behavior.
- [ ] Color contrast and focus states meet WCAG AA.
- [ ] Layout works at mobile, tablet, desktop, and wide sizes.
- [ ] Copy is specific, concise, and action-oriented.
- [ ] Components reuse or extend the existing design system.
- [ ] `references/ui-ux-frontend-implementation-rules.md` has been followed for frontend implementation.
- [ ] If top-brand inspiration is used, the output blends methods instead of copying a brand exactly.
- [ ] Developer handoff includes tokens, states, data needs, and QA steps.
- [ ] Risks, assumptions, and open questions are documented.

## Supporting Files

Use the supporting files in this skill folder when useful:

- `references/ui-ux-complete-checklist.md` — exhaustive checklist across UX, UI, content, accessibility, states, responsiveness, and handoff.
- `references/ui-ux-frontend-implementation-rules.md` — mandatory frontend implementation rules so agents do not miss stack inspection, states, accessibility, responsiveness, tokens, QA, or handoff.
- `references/wcag-aa-quick-reference.md` — practical WCAG 2.2 AA reference for agents.
- `references/design-system-playbook.md` — how to create or extend a design system.
- `references/top-100-brand-website-analysis.md` — top 100 global brand website patterns and reusable frontend methods.
- `templates/ui-ux-brief.md` — intake and requirements template.
- `templates/ui-ux-audit-report.md` — audit output template.
- `templates/component-spec.md` — component handoff template.
- `templates/design-system-spec.md` — design system template.
- `templates/top-brand-frontend-spec.md` — frontend spec template for top-brand-inspired UI.
- `scripts/validate_skill.py` — local validation for this skill package.
