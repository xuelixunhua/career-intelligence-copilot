---
name: career-intelligence-copilot
description: Maintain a full career-intelligence workflow inside a project. Use this skill whenever the user wants to collect job postings, update a master dataset, analyze the job market, rank real companies, reverse-engineer resume strategy from real job samples, maintain a workbook or decision board, or turn repeated job-search research into a reusable operating system. This skill is especially useful for recurring weekly updates, browser-based collection, and evidence-driven resume improvement.
---

# Career Intelligence Copilot

## Goal

Treat job-search research as one connected pipeline:

1. collect postings
2. maintain a deduplicated master dataset
3. analyze the market
4. identify target companies
5. reverse-engineer resume direction from real jobs
6. update the decision system

Do not treat these as unrelated one-off tasks unless the user explicitly wants only a single step.

## Read First

Start with:

- `references/file-map.md`
- `references/workbook-rules.md`

If the task involves company ranking or resume guidance, also read:

- `references/real-role-derived-guidance.md`
- `references/adaptation-guide.md`

If the task involves browser-based web work, use [$web-access](C:/Users/xueli/.codex/skills/web-access/SKILL.md).
If the task involves resume PDFs, use [$pdf](C:/Users/xueli/.codex/skills/pdf/SKILL.md).
If the task involves spreadsheet maintenance, use [$xlsx](C:/Users/xueli/.agents/skills/xlsx/SKILL.md).

## Working Model

### 1. Collection Principles

- Prefer real browser interaction for modern job sites
- Preserve login state locally, not in the repository
- Filter out obvious low-value records such as headhunters, anonymous employers, or postings with missing critical fields
- Maintain trend fields such as run date, first seen, last seen, and seen count when the project tracks recurring updates

### 2. Analysis Principles

- Do not stop at counting postings
- Reorganize the market by business logic when useful:
  - company type
  - pay level
  - company size
  - role cluster
  - platform differences
- Separate market description from personal recommendation

### 3. Resume Guidance Principles

- Base advice on real sampled jobs whenever possible
- Explain why the market rewards a capability, not just what the user should learn
- Map role requirements into:
  - positioning
  - missing labels
  - project experience to build
  - resume rewrites

### 4. Decision Board Principles

- Treat the workbook as a decision system, not a scratchpad
- Keep company ranking, market conclusions, and personal positioning in sync

## Standard Flow

### A. When the user wants to update jobs

1. Read the current master dataset
2. Collect new postings from the relevant platforms
3. Apply filtering rules
4. Deduplicate into the master dataset
5. Update trend fields

### B. When the user wants market analysis

1. Read the latest accepted sample
2. Cluster the market into useful structures
3. Summarize pay, role, company, and platform patterns
4. Sync conclusions into the project outputs

### C. When the user wants company ranking

1. Read the workbook and latest sample
2. Use only real companies from the sampled dataset unless the user explicitly requests a broader strategy list
3. Assign representative roles
4. Rank companies using both market quality and personal fit
5. Write reasoning, not just scores

### D. When the user wants resume reverse-engineering

1. Read the latest resume
2. Read the sampled job dataset
3. Extract recurring capability signals
4. Pick representative roles as evidence
5. Rewrite advice into:
   - target role direction
   - missing labels
   - project ideas
   - resume wording changes

### E. When the user wants to productize the workflow

1. Update this project skill first
2. Add or refine references
3. Avoid scattering long-lived rules across random notes

## What To Tell The User

At the end of a run, make clear:

1. what files were updated
2. how many records are in the master dataset
3. which companies currently rank highest and why
4. what the user most needs to strengthen next
5. whether any old or temporary files were cleaned up
