---
name: signal-monitoring-to-action-swarm
description: "Run a multi-agent monitoring workflow that triages ongoing account, market, hiring, product, and executive signals into a ranked action queue. Use when the user wants watchlist triage and action planning rather than fresh target-account generation."
---

# Signal Monitoring To Action Swarm

## Overview

Use this swarm to convert noisy signals across a watchlist, territory, or account book into a focused set of action-worthy moves.

This is a swarm for ongoing monitoring and triage. It works best when there are many possible events and the user needs help deciding what changed, what matters now, and which few actions deserve attention.

## When to Use

- Use when the user wants signal monitoring with recommendations, not just an alert feed.
- Use when the task is to triage changes across named accounts, a territory, or a watchlist the user already cares about.
- Use when signals may come from hiring, launches, leadership changes, funding, market moves, or product activity.
- Use when the goal is to identify action-worthy events for accounts, territories, or segments.

## When Not to Use

- Do not use for one-off account research.
- Do not use when the user wants a fresh ranked target-account list, stakeholder map, or outreach hypotheses from scratch; route to `pipeline-generation-swarm`.
- Do not use when the user only wants the raw signals with no prioritization.
- Do not use for a live deal next-step question; route to the deal swarm instead.

## Swarm Lanes

Launch four read-only sub-agents.

### Lane 1: Event Monitor

Collect and summarize:

- leadership changes
- hiring spikes
- funding, M&A, or restructuring
- launches, partnerships, or product announcements
- account-level operational changes

### Lane 2: Significance Analyst

Decide:

- why each signal may matter
- whether it indicates urgency, budget, reorg, or shifting priorities
- which signals are likely noise

### Lane 3: Relationship Impact Mapper

Check:

- which existing accounts, contacts, or opportunities are affected
- where the signal changes the current plan
- where there is no real relationship path yet

### Lane 4: Action Planner

Recommend:

- immediate follow-up actions
- good next questions
- whether to monitor, research deeper, reach out, or ignore
- priority and confidence

## Workflow

1. Define the monitoring scope and time window.
2. Build an intent packet:
   - accounts, territory, or watchlist
   - signal categories of interest
   - user role
   - action constraints
3. Launch the four read-only lanes in parallel.
4. Synthesize the signals into a ranked action queue.
5. Keep the final output sparse and evidence-backed.

## Output Contract

Return:

1. `Scope`
2. `Ranked Signals`
3. `Why They Matter`
4. `Affected Accounts Or Relationships`
5. `Recommended Actions`
6. `Ignore Or Watchlist Items`

Each ranked signal should include confidence and a short explanation of why it made the cut.

## Approval Boundaries

- Do not send alerts, messages, or CRM updates unless the user asks explicitly.
- Do not treat social buzz as a strong signal without evidence.
- Do not convert a watchlist event into an urgent action just to fill the list.

## Failure Shields

- Do not return a raw event log and call it prioritization.
- Do not overfit to flashy announcements while ignoring context.
- Do not recommend the same action for every signal.
- Do not hide weak confidence behind polished wording.
- Do not drift into full target-account generation when the user asked for signal triage.
