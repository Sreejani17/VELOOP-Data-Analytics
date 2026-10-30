# Data Pipeline Proposal

## Proposed architecture
Product services / app events → ingestion (API, queue or batch export) → immutable raw storage → validation and quarantine → standardized staging tables → analytics marts → BI dashboards.

## Layers
- Raw: source-faithful, append-only, restricted access.
- Staging: normalized timestamps, enums, identifiers and types.
- Curated marts: user lifecycle, task funnel, rewards ledger, wallet/withdrawals, referrals and daily engagement.
- Semantic layer: approved KPI definitions.

## Operational controls
Schema versioning, lineage, row-count reconciliation, freshness SLA, retry/idempotency, dead-letter handling, access logs, secrets management, backup and recovery.

## Refresh proposal
Near-real-time for operational withdrawal monitoring only if needed and supported; otherwise hourly/daily batch based on business needs. Confirm SLA with stakeholders.
