---
name: sales-materials-swarm
description: "Run a multi-agent sales materials workflow that turns a sales narrative into decks, outreach assets, demo structure, proof packaging, and reusable collateral. Use when the user needs practical sales materials rather than only a higher-level narrative."
---

# Sales Materials Swarm

## Overview

Use this swarm to turn a rough or validated sales story into reusable materials a seller or operator can actually put in front of prospects.

This swarm breaks the work into presentation structure, outreach assets, demo flow, and proof packaging so the final result is a usable material plan rather than abstract messaging advice.

The job is not to perfect design polish. The job is to create clear sales materials that help the team engage, pitch, and follow up faster.

## When to Use

- Use when the team has the core story but needs decks, talk tracks, templates, demo structure, or proof packaging.
- Use when the goal is to equip the team with reusable materials instead of rewriting the narrative again.
- Use when the output should help with prospecting, discovery, demos, or follow-up.

## When Not to Use

- Do not use for a single outbound message or one-off email draft.
- Do not use when the underlying narrative is still unclear; route to `sales-narrative-swarm` first.
- Do not use when the user needs live deal strategy or close planning; route to a narrower swarm instead.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Sales Deck Architect

Ask this sub-agent to define:

- core slide arc
- section breakdown
- what to show versus what to say
- where customization should happen

This lane should optimize for clarity and reuse.

### Lane 2: Outreach Asset Planner

Ask this sub-agent to map:

- email and call asset needs
- supporting snippets and attachments
- how materials should support appointment setting
- missing pieces that block outreach

This lane should avoid writing a full campaign unless asked.

### Lane 3: Demo Flow Designer

Ask this sub-agent to design:

- demo structure
- key screens or product moments
- transitions from presentation into demo
- follow-up assets needed after the call

This lane should optimize for buyer comprehension, not feature dumping.

### Lane 4: Proof And Collateral Reviewer

Ask this sub-agent to inspect:

- proof points that belong in the materials
- case study or metric gaps
- objection-handling assets
- lightweight collateral to prioritize next

This lane should not invent evidence or collateral.

## Workflow

1. Define the selling context, audience, and materials gap.
2. Build a short intent packet:
   - current sales narrative or rough story
   - target buyer and use case
   - current materials if any
   - known proof points
   - stage of the sales cycle these materials support
3. Launch the four read-only lanes in parallel.
4. Merge the results into one practical materials plan.
5. End with the minimum set of materials the team should build or revise next.

## Output Contract

Return:

1. `Materials Goal`
2. `Core Narrative Coverage`
3. `Deck And Presentation Plan`
4. `Outreach And Demo Assets`
5. `Proof And Supporting Collateral`
6. `Recommended Next Actions`

## Approval Boundaries

- Do not claim assets exist if the user has not provided them.
- Do not invent proof, metrics, logos, or customer quotes.
- Do not publish or rewrite external collateral unless the user asks explicitly.

## Failure Shields

- Do not confuse messaging advice with usable sales materials.
- Do not recommend polished collateral that exceeds the team’s current stage needs.
- Do not overload early-stage decks or demos with unnecessary detail.
- Do not separate demo flow from the narrative it is supposed to support.
