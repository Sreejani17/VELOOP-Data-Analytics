# Wallet & Withdrawal Analytics Specification

## Wallet model
Treat the wallet as a ledger of immutable transactions. Derive balance from opening balance plus signed successful entries, unless the platform owner confirms a separate authoritative balance service.

## Transaction properties
wallet_txn_id, user_id, txn_type, amount_minor_units, currency, status, created_at, effective_at, reference_type, reference_id, idempotency_key and failure_code.

## Withdrawal lifecycle
requested → validated → processing → paid / rejected / cancelled / failed (confirm exact allowed transitions).

## Operational measures
Request volume, amount requested, paid amount, approval rate, rejection rate, failure rate, pending backlog, average/median processing time and age of oldest pending request.

## Controls
Use decimal or integer minor currency units, not floating-point money. Prevent duplicate payout processing with idempotency keys. Restrict payout details and expose only operationally necessary data to analytics.
