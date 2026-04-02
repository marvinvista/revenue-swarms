---
name: sales-narrative-swarm
description: "Run a multi-agent sales narrative workflow that turns product context, buyer pain, proof, and objections into a clear sales story. Use when the user needs sharper positioning and a repeatable sales narrative rather than ad hoc messaging."
---

# Sales Narrative Swarm

## Overview

Use this swarm to turn a fuzzy sales story into a clear narrative a seller or operator can actually use.

This swarm breaks the problem into buyer pain, value framing, proof, and objection handling so the final output is more rigorous than one person's instinctive pitch rewrite.

The job is not to produce brand copy. The job is to build a sales narrative that helps real conversations go better.

## When to Use

- Use when the user needs to sharpen how they explain the product in sales conversations.
- Use when the team has product context and customer signals, but the story still feels muddy or inconsistent.
- Use when the output should help with discovery, demos, objection handling, or live selling.

## When Not to Use

- Do not use for polishing one email or one landing-page headline.
- Do not use when the user already has a strong narrative and only needs outreach sequencing.
- Do not use when the problem is account selection or lead prioritization; route to a narrower swarm instead.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Buyer Pain Analyst

Ask this sub-agent to identify and structure:

- target buyer roles
- high-frequency pain points
- operational or strategic pressures
- why those pains matter now

This lane should distinguish strong evidence from loose assumptions.

### Lane 2: Value Proposition Designer

Ask this sub-agent to define:

- the product promise
- value framing by buyer type
- problem-to-outcome logic
- where the offer feels differentiated

This lane should avoid vague benefit language.

### Lane 3: Proof And Objection Analyst

Ask this sub-agent to inspect:

- available proof points
- likely skepticism
- objection patterns
- missing evidence that weakens the story

This lane should not invent proof.

### Lane 4: Narrative Packaging Reviewer

Ask this sub-agent to package and pressure-test:

- the core narrative arc
- language consistency
- talk tracks that are too broad or too technical
- message gaps that would confuse a buyer

This lane should optimize for clarity, not cleverness.

## Workflow

1. Define the product, target market, and selling context.
2. Build a short intent packet:
   - product and category
   - target buyer or ICP
   - current narrative if one exists
   - known proof points
   - known objections or confusion points
3. Launch the four read-only lanes in parallel.
4. Merge the results into one usable narrative.
5. End with a small set of narrative changes the team should actually make next.

## Output Contract

Return:

1. `Target Buyer And Pain`
2. `Narrative Core`
3. `Proof And Differentiation`
4. `Objections And Weak Spots`
5. `Recommended Next Actions`

## Approval Boundaries

- Do not claim proof that the user does not actually have.
- Do not present inferred buyer pain as verified customer truth.
- Do not rewrite external assets or publish messaging unless the user asks explicitly.

## Failure Shields

- Do not produce generic positioning language with no buyer specificity.
- Do not collapse multiple buyer personas into one blurry narrative.
- Do not treat objections as copywriting problems when they are really evidence gaps.
- Do not optimize for slogans instead of sales usefulness.
