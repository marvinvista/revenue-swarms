# Security

## Reporting A Vulnerability

Please do not open a public GitHub issue for suspected security problems.

Report vulnerabilities privately to the project maintainer with:

- a short description of the issue
- affected files or swarms
- reproduction steps if available
- potential impact

## Scope

This repository is mostly markdown, metadata, and lightweight local validation scripts. The primary risks are:

- accidentally publishing secrets or private URLs
- adding unsafe automation instructions to public swarms
- growing repo scripts beyond simple, inspectable behavior

## Expectations For Contributions

- Never commit credentials, tokens, or private company material.
- Treat public swarm content as publishable by default.
- Keep scripts compact and explicit.
- Flag any change that adds network access, external execution, or credential handling.
