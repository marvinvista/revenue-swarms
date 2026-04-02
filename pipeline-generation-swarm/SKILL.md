---
name: pipeline-generation-swarm
description: "Run a multi-agent pipeline generation workflow that builds or refreshes a ranked target-account plan from market signals, fit, stakeholder clues, and outreach hypotheses. Use when the user wants net-new pipeline creation rather than ongoing signal triage or one-off research."
---

# Pipeline Generation Swarm

## Overview

Use this swarm to turn a messy market, segment, or account universe into a fresh ranked pipeline plan.

This swarm is best when the user wants to decide which accounts should enter the pipeline next. It combines signal detection, account fit analysis, stakeholder mapping, and outreach hypothesis design so the final output is a ranked target-account plan ready for human review and follow-through.

## When to Use

- Use when the user wants to build or refresh a target-account list for net-new pipeline.
- Use when the task depends on multiple inputs such as fit, timing signals, likely stakeholders, and why-now angles.
- Use when the goal is to decide which accounts deserve outbound attention next, not just what changed in the market.

## When Not to Use

- Do not use for a single-account deep dive.
- Do not use when the task starts from an ongoing watchlist or alert stream and the real question is which events matter now; route to `signal-monitoring-to-action-swarm`.
- Do not use when the task is already an active deal strategy.
- Do not use for writing one outreach message in isolation.

## Swarm Lanes

Launch four read-only sub-agents.

### Lane 1: Signal Scout

Collect and rank:

- market signals that help score account attractiveness
- hiring signals that suggest fit or timing
- product and launch signals that create a reason to care
- executive or org-change signals that may open a window
- timing events that may indicate urgency

### Lane 2: Account Fit Analyst

Evaluate:

- ICP fit
- likely use-case fit
- disqualifiers
- account prioritization logic

This lane should explicitly mark weak-fit accounts instead of pushing everything forward.

### Lane 3: Stakeholder Mapper

Map:

- probable buying roles
- likely entry points
- relationship gaps
- where coverage is too thin to act confidently

### Lane 4: Outreach Hypothesis Builder

Develop:

- why-now hypotheses
- value angles
- talk tracks or subject-line hooks
- recommended first-touch approach

This lane should produce hypotheses, not pretend certainty.

## Workflow

1. Define the pipeline goal:
   - segment
   - product or motion
   - territory or account universe
   - time horizon
2. Build a short intent packet and launch the four lanes in parallel.
3. Synthesize the findings into a ranked target list.
4. Include both reasons to pursue and reasons to deprioritize.
5. End with approval-ready next actions rather than raw notes.

## Output Contract

Return:

1. `Pipeline Goal`
2. `Ranked Target Accounts`
3. `Why Now`
4. `Likely Stakeholders`
5. `Outreach Hypotheses`
6. `Recommended Next Actions`
7. `Accounts To Deprioritize`

## Approval Boundaries

- Do not send outreach or mutate systems automatically.
- Do not invent contacts, firmographic facts, or buying intent.
- Do not flatten all scoring into one opaque rank without explanation.

## Failure Shields

- Do not return a long company list with no prioritization.
- Do not treat every signal as meaningful.
- Do not let weak-fit accounts survive only because they are noisy in public data.
- Do not confuse outreach ideas with verified account insight.
- Do not return an event watchlist when the user asked for new target-account generation.
