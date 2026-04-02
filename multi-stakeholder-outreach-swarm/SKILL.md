---
name: multi-stakeholder-outreach-swarm
description: "Run a multi-agent outreach planning workflow that maps the buying committee, develops persona-specific messaging, sequences touches across stakeholders, and packages approval-ready actions. Use when the user wants coordinated account penetration instead of a single email draft."
---

# Multi-Stakeholder Outreach Swarm

## Overview

Use this swarm when a target account requires coordinated outreach across multiple people, roles, or buying committee layers.

This is not a single-message drafting workflow. It is a planning swarm that maps the audience, creates differentiated messaging, sequences the touches, and checks consistency before any human-approved send happens.

## When to Use

- Use when the user wants coordinated account penetration.
- Use when the outreach should involve multiple stakeholders with different roles or motivations.
- Use when the hardest problem is orchestration, not sentence-level copy.

## When Not to Use

- Do not use for a one-off email draft.
- Do not use when there is no plausible buying committee or multi-contact strategy.
- Do not use for pipeline prioritization or account research alone.

## Swarm Lanes

Launch four read-only sub-agents.

### Lane 1: Buying Committee Mapper

Map:

- likely evaluator, champion, economic buyer, executive sponsor, blocker
- role relationships
- where contact coverage is thin
- who should be approached first and why

### Lane 2: Persona Messaging Designer

Design role-specific messaging for:

- technical audiences
- business or operational audiences
- executive audiences
- procurement or risk-conscious audiences

Each message angle should explain why it fits that persona.

### Lane 3: Sequence Orchestrator

Plan:

- touch order
- channel order if relevant
- time spacing
- handoffs between stakeholders
- escalation paths when replies land from the wrong or unexpected contact

### Lane 4: Consistency And Risk Reviewer

Check for:

- contradictory promises across personas
- over-personalization or invented detail
- message overlap or fatigue risk
- claims that need human review before use

## Workflow

1. Define the target account, product, and outreach goal.
2. Build an intent packet:
   - target account
   - why now
   - known contacts
   - target outcome
   - constraints such as tone, compliance, or channels
3. Launch the four read-only lanes in parallel.
4. Merge the work into one coordinated outreach plan.
5. Return approval-ready actions and drafts, but do not send anything.

## Output Contract

Return:

1. `Target Stakeholder Map`
2. `Persona Messaging Matrix`
3. `Proposed Sequence`
4. `Risks And Consistency Checks`
5. `Approval-Ready Next Actions`

When useful, include short example message hooks per persona, not full long sequences unless the user asks for them.

## Approval Boundaries

- Do not send outreach automatically.
- Do not invent personal details, relationship history, or internal priorities.
- Do not claim compliance approval, legal approval, or executive support that has not been established.

## Failure Shields

- Do not produce five versions of the same message and call it a strategy.
- Do not mistake a contact list for a buying committee map.
- Do not optimize for clever copy while ignoring timing and sequencing.
- Do not let persona-specific messaging drift into contradiction.
