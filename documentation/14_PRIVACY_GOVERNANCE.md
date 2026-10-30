# Privacy & Data Governance Proposal

## Principles
Purpose limitation, data minimization, least privilege, transparency, retention limitation, security by design and auditable access.

## Controls
- Use pseudonymous analytics identifiers.
- Keep direct identifiers and payment details out of general analytics tables.
- Restrict raw data and sensitive operational fields by role.
- Encrypt data in transit and at rest using approved organizational controls.
- Define retention and deletion workflows with legal/privacy owners.
- Log access and exports.
- Mask or aggregate small cohorts where re-identification risk exists.
- Never place credentials, tokens or personal customer data in GitHub.

## Governance roles
Product owner approves event meaning; engineering owns instrumentation; data owner approves definitions and quality; finance approves monetary/reward valuation; privacy/legal approves processing, retention and access; analyst maintains documentation and tests.
