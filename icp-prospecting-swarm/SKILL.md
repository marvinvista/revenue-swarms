---
name: icp-prospecting-swarm
description: "Run a multi-agent ICP and prospecting workflow that defines target buyers, ranks buying signals, and maps likely entry points for outreach. Use when the user needs a clearer prospecting strategy rather than a one-off account brief."
---

# ICP Prospecting Swarm

## Overview

Use this swarm to make prospecting more disciplined before the team starts firing outreach.

This swarm combines ICP definition, signal detection, prioritization, and contact-entry logic so the output is a real prospecting plan instead of a loose list of companies.

The job is not to maximize surface area. The job is to identify who the team should actually go after and why.

## When to Use

- Use when the user needs to define or tighten the ideal customer profile.
- Use when prospecting quality matters more than raw list volume.
- Use when the output should connect ICP logic to actual sourcing and entry points.

## When Not to Use

- Do not use for a deep single-account strategy.
- Do not use when the user already has a clean target list and only needs outreach copy.
- Do not use when the work is really inbound qualification or live deal strategy.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: ICP Definition Analyst

Ask this sub-agent to define:

- best-fit customer shape
- buyer and team characteristics
- environment and use-case markers
- strongest fit boundaries

This lane should identify both positive traits and exclusions.

### Lane 2: Signal And Trigger Scout

Ask this sub-agent to find:

- demand signals
- growth or hiring indicators
- operational triggers
- timing events that suggest prospecting readiness

This lane should separate meaningful signals from noise.

### Lane 3: Account Prioritization Analyst

Ask this sub-agent to rank:

- likely target segments
- account classes
- reasons to prioritize
- reasons to deprioritize

This lane should avoid opaque scoring.

### Lane 4: Entry Point Mapper

Ask this sub-agent to map:

- likely buyer roles
- first-contact options
- stakeholder paths
- where the team lacks enough context to act confidently

This lane should not invent named contacts.

## Workflow

1. Define the product, motion, and prospecting objective.
2. Build a short intent packet:
   - product and category
   - current or intended ICP
   - territory or segment
   - known wins or losses
   - constraints such as ACV, sales cycle, or team bandwidth
3. Launch the four read-only lanes in parallel.
4. Merge the work into one prospecting plan.
5. End with a clear recommendation about where the team should start and where it should not.

## Output Contract

Return:

1. `ICP Definition`
2. `Priority Signals`
3. `Ranked Prospect Segments Or Accounts`
4. `Likely Entry Points`
5. `Prospecting Plan`
6. `Disqualifiers And Watchouts`

## Approval Boundaries

- Do not invent named contacts, budget, or buying intent.
- Do not present weak-fit segments as high-confidence targets.
- Do not start outreach automatically unless the user asks explicitly.

## Failure Shields

- Do not return a broad TAM view and call it an ICP.
- Do not let noisy public signals dominate fit logic.
- Do not hide disqualifiers in fine print.
- Do not confuse entry points with verified stakeholder knowledge.
