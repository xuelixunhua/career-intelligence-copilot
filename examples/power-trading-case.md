# Example Case: Beijing Power Trading Workflow

This repository can be used for a power-trading job-search workflow.

The example is intentionally domain-specific, but all data here is illustrative and sanitized.

## Workflow

1. Collect Beijing power-trading roles from Boss Zhipin and Liepin.
2. Remove headhunters, anonymous companies, and parsing-noise records.
3. Normalize accepted postings into an incoming JSON file.
4. Merge incoming rows into a guarded master dataset.
5. Analyze market structure, company type, salary band, and role requirements.
6. Rank real companies by fit, risk, pay certainty, and capability growth.
7. Reverse-engineer resume and portfolio upgrades from real role requirements.

## Example Search Keywords

- `电力交易`
- `AI 电力交易`
- `power trading`
- `energy trading`

## Example Role Buckets

- asset-side trading strategy
- user-side energy procurement
- storage and ancillary-services optimization
- trading platform product / solution roles
- integrated energy and aggregation roles

## Why This Example Matters

The domain is not the point.

The reusable pattern is:

```text
real postings -> normalized dataset -> market structure -> decision board -> resume evidence
```

For another domain, replace the keywords, company buckets, scoring criteria, and resume-evidence mapping.
