---
name: customer-success-swarm
description: "Run a multi-agent customer success workflow that turns a newly won or active customer into an onboarding, adoption, renewal, and expansion plan. Use when the user needs a disciplined customer success view rather than only a post-sale status update."
---

# Customer Success Swarm

## Overview

Use this swarm to turn a newly won or active customer into a practical post-sale success plan that protects renewal potential and creates upside.

This swarm breaks the work into implementation, adoption, renewal risk, and reference readiness so the final output is a usable success plan rather than a vague reminder to check in with the customer.

The job is not to manage a ticket queue. The job is to help the team get the customer to value quickly, keep them healthy, and create the conditions for renewal and expansion.

## When to Use

- Use when a deal has closed and the team needs an onboarding or implementation plan.
- Use when the customer is active but adoption, value realization, renewal risk, or expansion timing feels unclear.
- Use when the output should help the team drive customer success, protect revenue, or create reference-worthy outcomes.

## When Not to Use

- Do not use for pre-sale deal strategy or close planning; route to a narrower swarm instead.
- Do not use for a single support-ticket answer or one-off bug triage.
- Do not use when the user only wants a plain customer recap with no success decision to make.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Onboarding And Implementation Planner

Ask this sub-agent to define:

- success milestones
- implementation steps
- owners and dependencies
- early-risk handoff gaps from sales

This lane should optimize for time-to-value.

### Lane 2: Adoption And Value Realization Analyst

Ask this sub-agent to inspect:

- expected usage behaviors
- signs the customer is or is not adopting
- promised outcomes versus observed outcomes
- gaps that prevent clear value realization

This lane should distinguish usage activity from real customer value.

### Lane 3: Renewal And Expansion Analyst

Ask this sub-agent to evaluate:

- renewal confidence
- commercial or stakeholder risks
- expansion signals
- timing for additional seats, teams, or use cases

This lane should not assume expansion without evidence.

### Lane 4: Risk And Reference Readiness Reviewer

Ask this sub-agent to review:

- churn risks
- executive-sponsor weakness
- support, trust, or expectation gaps
- conditions for references, testimonials, or advocacy

This lane should surface uncomfortable risk clearly.

## Workflow

1. Define the customer, the current stage, and the post-sale decision to make.
2. Build a short intent packet:
   - what was sold and to whom
   - promised outcomes or ROI
   - current implementation or adoption status
   - known stakeholders
   - known risks, asks, or expansion opportunities
3. Launch the four read-only lanes in parallel.
4. Merge the results into one practical customer success plan.
5. End with the smallest set of actions that most increases customer health and renewal confidence.

## Output Contract

Return:

1. `Customer Success Goal`
2. `Implementation And Onboarding Plan`
3. `Adoption And Value Signals`
4. `Renewal And Expansion Risks`
5. `Reference And Advocacy Readiness`
6. `Recommended Next Actions`

## Approval Boundaries

- Do not claim the customer is healthy, renewing, or expanding without evidence.
- Do not invent adoption data, ROI, stakeholder buy-in, or reference willingness.
- Do not commit the customer to timelines, commercial terms, or deliverables unless the user asks explicitly.

## Failure Shields

- Do not confuse support responsiveness with customer success.
- Do not treat implementation completion as proof of value realization.
- Do not hide churn or sponsor risk behind optimistic language.
- Do not recommend expansion before the customer is clearly getting value.
