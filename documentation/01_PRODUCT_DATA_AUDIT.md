# Product Data Audit

## Audit approach
Map each product capability to the user action, system action, business outcome, required data, proposed event, source system and business question. The editable coverage matrix is `workbooks/02_Product_Data_Coverage_Matrix.xlsx`.

## Product areas in scope
- Account and registration
- Authentication and user lifecycle
- Task discovery and task lifecycle
- Rewards earning, credit and reversal
- Wallet balance and ledger transactions
- Withdrawal request and payout lifecycle
- Referral invitation, attribution and qualification
- Engagement, sessions and notifications
- Support interactions and operational exceptions

## Initial analytics gaps to verify
1. Is there a stable cross-system user identifier?
2. Are anonymous events supported, and how are they later linked?
3. Is a task attempt assigned a unique immutable ID?
4. Are task states and allowed transitions documented?
5. Is task completion validated server-side?
6. Is reward issuance represented by an auditable ledger?
7. Are reward reversals recorded as separate compensating entries?
8. Are wallet transactions immutable and idempotent?
9. Is there a single definition of available, pending and locked balance?
10. Are withdrawal status transitions and failure reasons standardized?
11. Is payout completion confirmed by a trusted payment provider callback?
12. Is referral attribution window and eligibility policy documented?
13. Are duplicate client event submissions prevented?
14. Are event timestamps UTC and timezone-aware?
15. Are platform and app-version taxonomies controlled?
16. Are test/internal accounts identifiable and excluded?
17. Are event delivery failures and retries observable?
18. Is data freshness monitored by source?
19. Are retention and deletion rules documented?
20. Are KPI definitions owned and approved by business stakeholders?

## Audit conclusion
The blueprint identifies the data needed for reliable analytics. Actual coverage cannot be certified until the authorized VELOOP dataset, schema and product owner confirmations are reviewed.
