---
name: deal-next-steps-swarm
description: "Run a multi-agent deal strategy workflow that analyzes deal state, communications, stakeholder coverage, risks, and timing to recommend the next best actions. Use when the user needs immediate guidance on an in-flight deal rather than a late-stage commit or forecast review."
---

# Deal Next Steps Swarm

## Overview

Use this swarm when an active deal needs strategic next-step guidance rather than a plain recap.

This swarm splits the problem into four independent lenses, then recombines them into an action plan. The output should tell the user what matters, what is missing, what is risky, and what to do next in priority order before the deal becomes a pure close-plan or forecast problem.

## When to Use

- Use when the user asks "what should I do next" on an opportunity, deal, or account in motion.
- Use when the answer depends on multiple evidence streams such as deal state, call notes, email history, stakeholder coverage, and timing.
- Use when a seller or operator needs a recommendation to move the deal forward, not just a summary.

## When Not to Use

- Do not use for a brand-new account with no deal context.
- Do not use when the primary question is whether the deal is truly closable this period, forecastable, or commercially ready to commit; route to `closing-pipeline-swarm`.
- Do not use for pipeline generation or outbound prospecting.
- Do not use when the user only wants a meeting recap or a single draft message.

## Swarm Lanes

Launch four read-only sub-agents for non-trivial deals.

### Lane 1: Deal State Analyst

Inspect:

- current stage and momentum
- recent progression or stagnation
- open dependencies
- missing deal hygiene or qualification elements

### Lane 2: Communication Analyst

Inspect:

- recent emails, calls, and meetings
- unanswered questions
- sentiment and urgency changes
- commitment signals or avoidance patterns

### Lane 3: Stakeholder Coverage Analyst

Inspect:

- who is involved
- who is missing
- whether access is too narrow
- likely champion, decision-maker, blocker, and evaluator gaps

### Lane 4: Risk And Timing Analyst

Inspect:

- timing pressure
- competitive threats
- procurement or legal friction
- reasons this deal may stall, slip, or die

## Workflow

1. Define the deal scope and objective of the analysis.
2. Build an intent packet:
   - account and opportunity name
   - deal stage if known
   - what outcome the user wants next
   - any constraints such as quarter end, meeting date, or stakeholder pressure
3. Launch the four read-only lanes in parallel.
4. Synthesize a ranked action plan.
5. Separate `must do now` from `helpful if time permits`.

## Output Contract

Return:

1. `Deal Snapshot`
2. `Signals From Recent Activity`
3. `Coverage Gaps`
4. `Top Risks`
5. `Recommended Next Actions`
6. `Open Questions`

The `Recommended Next Actions` section should be prioritized and concrete.

## Approval Boundaries

- Do not update CRM, change deal stage, send emails, or commit to external actions unless explicitly asked.
- Do not confuse a guess about stakeholder intent with a verified commitment.
- Do not claim a deal is healthy when the evidence is mixed.

## Failure Shields

- Do not output "follow up" as a plan without saying with whom, why, and toward what outcome.
- Do not hide missing stakeholder coverage behind optimistic language.
- Do not let one positive signal erase a broad pattern of drift or avoidance.
- Do not return a summary when the user asked for a recommendation.
- Do not drift into generic forecast theater when the real need is a concrete next move.
