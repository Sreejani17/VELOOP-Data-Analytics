# Data Quality Rules

| Dimension | Rule | Severity | Action |
|---|---|---|---|
| Completeness | Required IDs and event timestamps are non-null | High | Quarantine invalid records |
| Uniqueness | Primary IDs are unique | High | Deduplicate with lineage |
| Validity | Dates parse and comply with expected ranges | High | Quarantine/fix producer |
| Validity | Status belongs to approved enum | Medium | Map only approved aliases |
| Accuracy | Amounts/points are numeric and within policy | High | Reject and investigate |
| Consistency | Currency and platform use controlled values | Medium | Normalize and validate |
| Referential integrity | Foreign keys map to parent entities | High | Quarantine or reconcile |
| Timeliness | Data arrives within source-specific SLA | Medium | Alert owner |
| Sequence | Completion/processing timestamps follow lifecycle | High | Investigate impossible transitions |
| Idempotency | Duplicate transaction/event submissions are suppressed | High | Use idempotency keys |
