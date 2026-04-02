---
name: outbound-appointment-setting-swarm
description: "Run a multi-agent outbound workflow that designs hooks, CTAs, sequencing, and reply handling to help book first meetings. Use when the user wants a repeatable meeting-setting plan rather than one draft message."
---

# Outbound Appointment Setting Swarm

## Overview

Use this swarm when the team needs a better path from cold outreach to a booked conversation.

This swarm focuses on meeting-setting mechanics: the hook, the ask, the sequence, and the response logic. The output should be a real outbound plan, not a pile of disconnected message drafts.

The job is to improve appointment-setting judgment, not to automatically send outreach.

## When to Use

- Use when the user wants to improve cold outbound or appointment setting.
- Use when the challenge is getting a first meeting, not running a full account penetration strategy.
- Use when the team needs stronger hooks, CTAs, sequencing, or reply handling.

## When Not to Use

- Do not use for one-off copy polish.
- Do not use when the user needs ICP definition before outreach.
- Do not use when the work requires a full buying-committee motion; route to the outreach swarm instead.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Offer And CTA Strategist

Ask this sub-agent to define:

- the outreach offer
- the meeting ask
- CTA strength
- friction points that make the ask easy or hard to accept

This lane should optimize for a real next step.

### Lane 2: Messaging Angle Designer

Ask this sub-agent to develop:

- opening hooks
- why-now angles
- role-specific message ideas
- positioning variations worth testing

This lane should avoid long-form copy unless the user asks for it.

### Lane 3: Sequence Planner

Ask this sub-agent to design:

- step order
- cadence logic
- channel mix if relevant
- when to stop or escalate

This lane should avoid over-sequencing for its own sake.

### Lane 4: Reply Handling Reviewer

Ask this sub-agent to inspect:

- likely positive replies
- soft objections
- brush-offs
- how the team should respond without losing momentum

This lane should not assume intent that is not there.

## Workflow

1. Define the target audience and meeting objective.
2. Build a short intent packet:
   - audience or account type
   - offer and product context
   - current outbound motion
   - target meeting outcome
   - constraints such as tone, channel, or compliance
3. Launch the four read-only lanes in parallel.
4. Merge the work into one meeting-setting plan.
5. End with approval-ready next actions, not just theory.

## Output Contract

Return:

1. `Target Audience`
2. `Primary Hooks`
3. `Meeting-Setting Sequence`
4. `Reply Handling`
5. `Risks And Adjustments`
6. `Approval-Ready Next Actions`

## Approval Boundaries

- Do not send outbound automatically.
- Do not invent personal details or false urgency.
- Do not claim relevance, proof, or relationships that are not established.

## Failure Shields

- Do not produce a generic sequence with no hook logic.
- Do not optimize for clever lines instead of booked meetings.
- Do not make the CTA vague.
- Do not treat every reply as a buying signal.
