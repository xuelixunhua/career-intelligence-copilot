# Master Dataset Merge

The master dataset must not be overwritten directly by temporary scraping scripts.

Use:

- `scripts/merge_master_dataset.py`
- `scripts/run_merge_master.cmd`

## Preconditions

Only merge when:

1. scraping has completed
2. records are normalized into an incoming JSON array
3. headhunters, anonymous companies, parsing noise, and incomplete rows have been filtered
4. post-scrape quality checks have passed

## Required Incoming Fields

Each incoming row must contain:

- `source_platform`
- `run_date`
- `search_keyword`
- `search_city_label`
- `job_id`
- `job_key`
- `source_url`
- `job_title`
- `accepted`

Recommended full fields:

- `company_name`
- `salary_text`
- `salary_min_k`
- `salary_max_k`
- `salary_months`
- `experience`
- `education`
- `city`
- `district`
- `business_district`
- `job_location`
- `industry`
- `financing_stage`
- `company_size`
- `recruiter_name`
- `recruiter_title`
- `company_intro`
- `job_description`
- `work_address`
- `detail_mode`
- `filter_reasons`

The merge script maintains:

- `first_seen_date`
- `last_seen_date`
- `seen_count`
- `seen_dates`

## Guards

The merge script should:

- require an explicit baseline row-count guard when a master dataset exists
- reject inconsistent CSV and JSON baselines
- reject unexpected shrinkage unless explicitly allowed
- create timestamped backups before replacement
- write files atomically
- optionally purge rejected historical rows when the workflow policy requires it

## Example

```powershell
scripts\run_merge_master.cmd `
  --incoming-json tmp\incoming\jobs_2026-05-05.json `
  --master-csv output\jobs_master.csv `
  --master-json output\jobs_master.json `
  --expected-existing-min 100 `
  --summary-json tmp\incoming\merge_summary_2026-05-05.json
```
