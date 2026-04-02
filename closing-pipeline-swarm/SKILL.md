---
name: closing-pipeline-swarm
description: "Run a multi-agent closing workflow that pressure-tests late-stage close plans, stakeholder coverage, commercial risk, and forecast realism. Use when the user needs a commit-grade close review rather than general next-step coaching."
---

# Closing Pipeline Swarm

## Overview

Use this swarm when an opportunity is late enough that the close date, commit call, or forecast accuracy is on the line.

This swarm looks at close mechanics from multiple lenses: deal reality, commercial process, stakeholder coverage, and plan quality. The output should help the user decide what is really closable, what forecast stance is defensible, and what is still wishful thinking.

The job is not to sound confident. The job is to increase closing discipline.

## When to Use

- Use when a deal is approaching close, commit, or forecast scrutiny.
- Use when the user needs a close plan and a pipeline reality check at the same time.
- Use when stakeholder, procurement, or commercial friction may shape whether the deal should actually be called.

## When Not to Use

- Do not use for early-stage discovery planning.
- Do not use for broad account research with no active deal motion.
- Do not use when the user mainly needs help deciding the immediate next play on an active deal before late-stage close pressure exists; route to `deal-next-steps-swarm`.
- Do not use when the user only needs a meeting follow-up draft.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Deal Reality Analyst

Ask this sub-agent to inspect:

- current deal health
- evidence of true progression
- slippage risk
- what is being assumed rather than known

This lane should challenge optimism bias directly.

### Lane 2: Commercial And Procurement Analyst

Ask this sub-agent to identify:

- pricing or packaging friction
- legal and procurement risk
- commercial blockers
- dependencies that affect close timing

This lane should make process risk visible early.

### Lane 3: Stakeholder And Champion Analyst

Ask this sub-agent to inspect:

- champion quality
- executive coverage
- blocker risk
- who still needs to be involved before close

This lane should not confuse access with alignment.

### Lane 4: Close Plan Reviewer

Ask this sub-agent to evaluate:

- the proposed close plan
- required next steps
- forecast realism
- fallback paths if the ideal plan fails

This lane should prioritize decision quality over perfect formatting.

## Workflow

1. Define the deal and the close or forecast decision that matters.
2. Build a short intent packet:
   - account and opportunity
   - current stage and target close date
   - forecast status if known
   - known stakeholders and blockers
   - known commercial or legal issues
3. Launch the four read-only lanes in parallel.
4. Merge the work into one close-readout.
5. End with clear next moves and a forecast stance.

## Output Contract

Return:

1. `Closing Snapshot`
2. `Reality Check`
3. `Commercial And Process Risks`
4. `Champion And Stakeholder Gaps`
5. `Close Plan`
6. `Fallback Paths`

## Approval Boundaries

- Do not change pipeline stage, forecast category, or CRM fields unless the user asks explicitly.
- Do not present hope as evidence.
- Do not imply procurement or legal approval that has not happened.

## Failure Shields

- Do not output a close plan with no dependencies.
- Do not let one friendly contact erase broad stakeholder risk.
- Do not hide commercial friction in vague language.
- Do not recommend commit behavior without a real reality check.
- Do not collapse into generic next-step advice without taking a forecast stance.
