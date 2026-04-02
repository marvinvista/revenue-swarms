---
name: inbound-qualification-swarm
description: "Run a multi-agent inbound qualification workflow that triages fit, urgency, routing, and disqualifiers for inbound interest. Use when the user needs a more disciplined decision about how to handle inbound demand rather than research a full account."
---

# Inbound Qualification Swarm

## Overview

Use this swarm when inbound demand needs judgment, not just queue management.

This swarm evaluates fit, urgency, routing, and disqualifiers in parallel so the output helps the team respond faster and more consistently.

The job is not to accept every inbound lead. The job is to decide what this inbound deserves next.

## When to Use

- Use when the user needs to triage demo requests, contact forms, or other inbound interest.
- Use when qualification depends on more than one signal, such as fit, urgency, context, and next-step routing.
- Use when the output should recommend what to do next with an inbound lead.

## When Not to Use

- Do not use for cold prospecting or account generation.
- Do not use for a live late-stage deal inspection.
- Do not use when the user only wants a summary of the inbound message.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Inquiry And Context Analyst

Ask this sub-agent to inspect:

- what the inbound actually asked for
- context and stated intent
- account clues
- signs of seriousness or vagueness

This lane should separate explicit asks from inferred intent.

### Lane 2: Qualification Analyst

Ask this sub-agent to evaluate:

- fit against ICP
- urgency and timing
- likely use-case strength
- whether the inbound deserves fast follow-up

This lane should avoid over-qualifying thin evidence.

### Lane 3: Routing And Response Planner

Ask this sub-agent to recommend:

- the best owner
- the right next meeting or response type
- questions that should be answered before advancing
- what speed of follow-up makes sense

This lane should optimize for the next move, not bureaucracy.

### Lane 4: Risk And Disqualification Reviewer

Ask this sub-agent to identify:

- mismatch signals
- low-intent patterns
- bad-fit indicators
- reasons the inbound should be parked, disqualified, or handled carefully

This lane should keep the team from chasing false positives.

## Workflow

1. Define the inbound source and the qualification decision to make.
2. Build a short intent packet:
   - inbound message or request
   - source and timing
   - known account context
   - product or motion
   - current routing rules if they exist
3. Launch the four read-only lanes in parallel.
4. Merge the work into one qualification recommendation.
5. End with a clear route, not a generic summary.

## Output Contract

Return:

1. `Inbound Snapshot`
2. `Qualification Read`
3. `Recommended Route`
4. `Questions To Resolve`
5. `Risks Or Disqualifiers`
6. `Recommended Next Actions`

## Approval Boundaries

- Do not mark a lead as qualified in external systems unless asked explicitly.
- Do not invent urgency, budget, or authority.
- Do not present a polite inquiry as high purchase intent without evidence.

## Failure Shields

- Do not confuse responsiveness with fit.
- Do not over-route low-signal inbounds into expensive sales time.
- Do not hide disqualification risk behind optimistic language.
- Do not return a summary when the user needs a decision.
