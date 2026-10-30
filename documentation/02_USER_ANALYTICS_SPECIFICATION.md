# User Analytics Specification

## Lifecycle
Acquisition → registration → activation → first meaningful task → repeat engagement → reward earning → wallet use → withdrawal or redemption → retention/reactivation.

## Core dimensions
- User ID (pseudonymous), signup date, acquisition source, platform, app version, geography at an appropriately coarse level, account status and cohort.
- Do not collect unnecessary direct identifiers in analytics events.

## Funnel definitions
1. Registration funnel: registration started → registration accepted.
2. Activation funnel: registration accepted → first qualifying task started/completed within an approved window.
3. Task funnel: task viewed → task started → task submitted → task validated.
4. Reward funnel: eligible completion → reward calculated → ledger credit committed.
5. Withdrawal funnel: request submitted → validated → processed → paid/rejected.

## Cohorts and retention
Use signup week/month cohorts. Define retained user as a user with at least one approved qualifying event in the selected return window. Confirm exact D1/D7/D30 window boundaries and timezone before publication.

## Segmentation
Acquisition source, signup cohort, platform, app version, task category and coarse geography. Avoid sensitive attributes unless specifically approved and legally justified.
