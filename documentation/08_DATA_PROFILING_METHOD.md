# Simulated Data Profiling Method

## Datasets represented
Users, Task_Activity, Rewards, Wallet, Withdrawals, Referrals, Feature_Events and Messy_Data.

## Profiling dimensions
- Record and column counts
- Missing cells by field
- Duplicate rows and duplicate primary keys
- Date/time parseability and min/max range
- Numeric min/max and negative-value checks
- Controlled category/status distributions
- Foreign-key orphans
- Duplicate event identifiers

## Interpretation
The CSVs in `data/sample/` are synthetic and exist only to demonstrate code execution. Their counts and patterns must not be reported as company facts. Run the profiler on the authorized assignment dataset for evidence-based findings.
