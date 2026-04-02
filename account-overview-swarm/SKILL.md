---
name: account-overview-swarm
description: "Run a multi-agent account brief workflow that combines verified company facts, strategic context, stakeholder coverage, risks, and synthesis into one decision-ready view. Use when the user wants a holistic account brief rather than a narrow lookup."
---

# Account Overview Swarm

## Overview

Use this swarm to build a decision-ready account brief from multiple independent lenses in parallel.

The main agent frames the account, launches specialized read-only sub-agents, then synthesizes the results into one coherent overview that a seller, operator, or account owner can actually act on.

The job is not to gather every possible fact. The job is to produce a compact account view that combines what is true, what is strategically important, what is still uncertain, and what to do next.

## When to Use

- Use when the user wants a complete account overview, account brief, account research packet, or account intelligence summary.
- Use when the task needs more than one data lens, such as company facts plus strategic context plus stakeholder mapping.
- Use when the final output should explain both what the account is and why it matters now.

## When Not to Use

- Do not use for a single-field lookup or one narrow fact question.
- Do not use when the user already has the account brief and only wants one email or one next step.
- Do not use when the work is really lead generation, deal strategy, or outreach sequencing; route to the narrower swarm instead.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Account Facts Scout

Ask this sub-agent to collect and normalize:

- firmographic basics
- product and business model facts
- geography, segment, and scale signals
- recent factual company updates

This lane should clearly separate verified facts from assumptions.

### Lane 2: Strategic Context Scout

Ask this sub-agent to infer and support:

- likely business priorities
- major initiatives and transformation pressures
- likely pain points or pressure areas
- why the account may be important now

This lane should cite the evidence behind each strategic claim.

### Lane 3: Relationship And Stakeholder Scout

Ask this sub-agent to inspect:

- known stakeholders
- probable buyer, champion, blocker, and influencer roles
- relationship coverage gaps
- org-chart or committee hypotheses

This lane should label low-confidence stakeholder inference explicitly.

### Lane 4: Opportunity And Risk Scout

Ask this sub-agent to identify:

- likely opportunity areas
- timing signals
- competitive or operational risks
- reasons the account may stall or be a poor fit

This lane should avoid wishful ranking and include disqualifiers.

## Workflow

1. Define the account scope and the decision the brief should support.
2. Build a short intent packet:
   - account name
   - why this brief is being requested
   - target role or use case
   - any known constraints such as territory, product line, or deal stage
3. Launch the four read-only lanes in parallel.
4. Merge results into one account brief:
   - deduplicate overlapping claims
   - preserve the strongest evidence
   - keep uncertainty visible
5. End with a focused set of next-step recommendations rather than a vague conclusion.

## Output Contract

Return a compact brief with these sections:

1. `Account Snapshot`
2. `Why This Account Matters`
3. `Strategic Context`
4. `Stakeholders And Relationship Coverage`
5. `Opportunity Areas`
6. `Risks And Unknowns`
7. `Recommended Next Actions`

## Approval Boundaries

- Do not send emails, update CRM, or create external artifacts unless the user asks for those actions explicitly.
- Do not present inferred pain points or stakeholder roles as verified facts.
- Do not bury uncertainty inside polished prose.

## Failure Shields

- Do not let one lane dominate the whole brief.
- Do not return a fact dump with no prioritization.
- Do not present generic company research as account strategy.
- Do not infer an opportunity where the stronger conclusion is "not enough evidence yet."
