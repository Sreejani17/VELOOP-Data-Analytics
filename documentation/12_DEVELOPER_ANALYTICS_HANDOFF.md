# Developer Analytics Handoff

## Event envelope
event_id, event_name, event_version, event_timestamp_utc, received_at_utc, user_id (nullable only for approved anonymous events), session_id, platform, app_version, environment, correlation_id and event_properties.

## Engineering requirements
- Generate stable event IDs and idempotency keys.
- Use snake_case event names and versioned schemas.
- Validate required properties before emission.
- Send authoritative business events server-side where possible.
- Keep client and server timestamps distinct.
- Avoid PII and secrets in event payloads.
- Provide retry behavior with deduplication.
- Document event ownership and schema changes.

## Handoff acceptance checklist
- Event trigger and business meaning approved.
- Required/optional properties documented.
- Example payload and schema validation tests available.
- Duplicate/retry behavior tested.
- User identity and anonymous behavior defined.
- Data owner and monitoring owner assigned.
