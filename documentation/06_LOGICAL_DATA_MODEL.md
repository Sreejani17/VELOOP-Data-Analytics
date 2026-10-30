# Logical Data Model

See `diagrams/velo_ops_erd.mmd`.

## Entities
- Users: one row per account.
- Task definitions: catalog of available tasks.
- Task activity: one row per user attempt.
- Rewards: immutable earning/reversal ledger.
- Wallet transactions: financial/points ledger.
- Withdrawals: payout requests and state transitions.
- Referrals: referrer-to-invitee attribution.
- Feature events: event stream for behavioral analytics.
- Sessions: optional session-level grouping.

## Relationship rules
Users 1-to-many task activity, rewards, wallet transactions, withdrawals, referrals as referrer, and feature events. Task activity may generate one or more reward ledger entries subject to business policy. Referrals may have zero or one matched referred user before registration. Every foreign key must be validated or quarantined.
