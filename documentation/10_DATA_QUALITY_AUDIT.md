# Data Quality Audit Report

## Scope
A repeatable audit is provided in `src/data_quality_audit.py`. It checks duplicate rows, missing values, duplicate candidate IDs, invalid timestamps, invalid numeric values, negative amounts/points and foreign-key orphans where applicable.

## Demonstration issues
`data/sample/Messy_Data.csv` intentionally contains examples of duplicate record IDs, missing user ID, malformed timestamp, unknown status, negative amount and non-numeric amount. These are constructed examples, not observed VELOOP defects.

## Run
```bash
python src/data_quality_audit.py --input data/sample --output reports/generated
```

## Remediation workflow
1. Preserve raw source data unchanged.
2. Generate issue-level records with dataset, key, rule and severity.
3. Quarantine invalid rows; do not silently drop them.
4. Correct upstream producer or mapping where possible.
5. Re-run checks and retain before/after counts.
6. Obtain data-owner sign-off for accepted exceptions.
