# Earning & Reward Analytics Specification

## Questions
- How many eligible activities generate rewards?
- What is the number and value of points credited, reversed and outstanding?
- How long between eligibility and ledger credit?
- Which task categories drive earning?
- What are the reward failure and reversal reasons?

## Recommended ledger fields
reward_id, user_id, source_activity_id, points, currency/point unit, status, created_at, effective_at, reversal_of_reward_id, reason_code, idempotency_key.

## Controls
- One committed reward per eligible source activity unless policy explicitly allows multiples.
- Reversal should be an auditable compensating entry, not destructive update.
- Reconcile reward ledger totals to wallet/points balance using approved accounting rules.
- Keep pending, credited, reversed and failed states distinct.
- Define point expiry and valuation only with approved business rules.
