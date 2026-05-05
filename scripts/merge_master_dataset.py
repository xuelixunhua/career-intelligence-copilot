# -*- coding: utf-8 -*-
"""
Canonical master-dataset merge entrypoint for the project-local skill.

Use this script after browser scraping has already produced a normalized
incoming JSON payload. It is intentionally strict so the master dataset
cannot be overwritten casually by ad hoc scripts.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterable


FIELDS = [
    "source_platform",
    "run_date",
    "search_keyword",
    "search_keywords",
    "search_city_label",
    "job_id",
    "job_key",
    "source_url",
    "job_title",
    "company_name",
    "salary_text",
    "salary_min_k",
    "salary_max_k",
    "salary_months",
    "experience",
    "education",
    "city",
    "district",
    "business_district",
    "job_location",
    "industry",
    "financing_stage",
    "company_size",
    "recruiter_name",
    "recruiter_title",
    "company_intro",
    "job_description",
    "work_address",
    "detail_mode",
    "accepted",
    "filter_reasons",
    "first_seen_date",
    "last_seen_date",
    "seen_count",
    "seen_dates",
]

REQUIRED_INCOMING_FIELDS = {
    "source_platform",
    "run_date",
    "search_keyword",
    "search_city_label",
    "job_id",
    "job_key",
    "source_url",
    "job_title",
    "accepted",
}

PRESERVE_FIELDS = {"first_seen_date", "last_seen_date", "seen_count", "seen_dates"}


class MergeGuardError(RuntimeError):
    pass


@dataclass
class LoadedMaster:
    rows: list[dict[str, str]]
    source: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Safely merge scraped rows into the master dataset.")
    parser.add_argument("--incoming-json", required=True, help="Path to normalized incoming rows JSON.")
    parser.add_argument(
        "--master-csv",
        default="output/jobs_master.csv",
        help="Existing master CSV path.",
    )
    parser.add_argument(
        "--master-json",
        default="output/jobs_master.json",
        help="Existing master JSON path.",
    )
    parser.add_argument(
        "--backup-dir",
        default="output/backups",
        help="Directory for timestamped backups before replacement.",
    )
    parser.add_argument(
        "--summary-json",
        default="",
        help="Optional path to write the merge summary JSON.",
    )
    parser.add_argument(
        "--expected-existing-min",
        type=int,
        default=None,
        help="Required minimum row count for an existing master before write is allowed.",
    )
    parser.add_argument(
        "--allow-initialize-empty-master",
        action="store_true",
        help="Allow creating a master from scratch when no baseline files exist.",
    )
    parser.add_argument(
        "--allow-shrink",
        action="store_true",
        help="Allow merged total rows to be smaller than the baseline count.",
    )
    parser.add_argument(
        "--drop-rejected-existing",
        action="store_true",
        help="Drop existing rows whose accepted field is not True before merging incoming rows.",
    )
    return parser.parse_args()


def normalize_scalar(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, (int, float)):
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)
    if isinstance(value, list):
        return "；".join(str(item).strip() for item in value if str(item).strip())
    return str(value).strip()


def normalize_row(raw: dict) -> dict[str, str]:
    row = {field: normalize_scalar(raw.get(field, "")) for field in FIELDS}
    for key in REQUIRED_INCOMING_FIELDS:
        if not row.get(key):
            raise MergeGuardError(f"Incoming row missing required field '{key}': {raw!r}")
    if not row["seen_count"]:
        row["seen_count"] = "1"
    return row


def load_json_rows(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise MergeGuardError(f"Incoming JSON must be an array: {path}")
    return [normalize_row(item) for item in payload]


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [{field: normalize_scalar(row.get(field, "")) for field in FIELDS} for row in csv.DictReader(handle)]


def load_master_rows(csv_path: Path, json_path: Path) -> LoadedMaster:
    csv_exists = csv_path.exists()
    json_exists = json_path.exists()

    if not csv_exists and not json_exists:
        return LoadedMaster(rows=[], source="missing")

    if csv_exists and not json_exists:
        return LoadedMaster(rows=load_csv_rows(csv_path), source="csv-only")

    if json_exists and not csv_exists:
        return LoadedMaster(rows=load_json_rows(json_path), source="json-only")

    csv_rows = load_csv_rows(csv_path)
    json_rows = load_json_rows(json_path)
    csv_keys = [row["job_key"] for row in csv_rows]
    json_keys = [row["job_key"] for row in json_rows]
    if csv_keys != json_keys:
        raise MergeGuardError(
            "Master CSV and JSON are inconsistent. Refusing to write until baseline is repaired."
        )
    return LoadedMaster(rows=csv_rows, source="csv+json")


def dedupe_incoming(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["job_key"]
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def is_accepted_row(row: dict[str, str]) -> bool:
    return normalize_scalar(row.get("accepted", "")).lower() == "true"


def backup_file(src: Path, backup_dir: Path, timestamp: str) -> str:
    if not src.exists():
        return ""
    backup_dir.mkdir(parents=True, exist_ok=True)
    dst = backup_dir / f"{src.stem}.{timestamp}{src.suffix}"
    shutil.copy2(src, dst)
    return str(dst)


def atomic_write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8-sig", newline="", delete=False, dir=path.parent, suffix=".tmp") as tmp:
        writer = csv.DictWriter(tmp, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDS})
        temp_path = Path(tmp.name)
    temp_path.replace(path)


def atomic_write_json(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp") as tmp:
        json.dump(rows, tmp, ensure_ascii=False, indent=2)
        temp_path = Path(tmp.name)
    temp_path.replace(path)


def merge_rows(existing_rows: list[dict[str, str]], incoming_rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict]:
    existing_by_key = {row["job_key"]: row for row in existing_rows if row.get("job_key")}
    created = 0
    updated = 0
    accepted = 0
    rejected = 0

    for row in incoming_rows:
        if row["accepted"] == "True":
            accepted += 1
        else:
            rejected += 1

        key = row["job_key"]
        run_date = row["run_date"]
        if key in existing_by_key:
            current = existing_by_key[key]
            previous_dates = [item for item in (current.get("seen_dates") or "").split("；") if item]
            for field, value in row.items():
                if field in PRESERVE_FIELDS:
                    continue
                current[field] = value
            if not current.get("first_seen_date"):
                current["first_seen_date"] = run_date
            if run_date not in previous_dates:
                previous_dates.append(run_date)
                try:
                    current["seen_count"] = str(int(current.get("seen_count") or "0") + 1)
                except ValueError:
                    current["seen_count"] = "1"
            current["last_seen_date"] = run_date
            current["seen_dates"] = "；".join(previous_dates)
            updated += 1
        else:
            new_row = {field: row.get(field, "") for field in FIELDS}
            new_row["first_seen_date"] = run_date
            new_row["last_seen_date"] = run_date
            new_row["seen_count"] = "1"
            new_row["seen_dates"] = run_date
            existing_rows.append(new_row)
            existing_by_key[key] = new_row
            created += 1

    merged_rows = sorted(
        existing_rows,
        key=lambda row: (row.get("source_platform", ""), row.get("company_name", ""), row.get("job_title", "")),
    )
    summary = {
        "incoming_rows": len(incoming_rows),
        "created_rows": created,
        "updated_rows": updated,
        "accepted_rows": accepted,
        "rejected_rows": rejected,
        "merged_total_rows": len(merged_rows),
    }
    return merged_rows, summary


def enforce_guards(
    master: LoadedMaster,
    merged_rows: list[dict[str, str]],
    args: argparse.Namespace,
) -> None:
    existing_count = len(master.rows)
    merged_count = len(merged_rows)

    if existing_count == 0:
        if master.source != "missing" and not args.allow_initialize_empty_master:
            raise MergeGuardError(
                "Baseline files exist but loaded as empty. Refusing to write without --allow-initialize-empty-master."
            )
        if master.source == "missing" and not args.allow_initialize_empty_master:
            raise MergeGuardError(
                "No baseline files found. Refusing to initialize a new master without --allow-initialize-empty-master."
            )
    else:
        if args.expected_existing_min is None:
            raise MergeGuardError(
                "Refusing to write an existing master without --expected-existing-min."
            )
        if existing_count < args.expected_existing_min:
            raise MergeGuardError(
                f"Baseline row count {existing_count} is below expected minimum {args.expected_existing_min}."
            )
        if merged_count < existing_count and not args.allow_shrink:
            raise MergeGuardError(
                f"Merged row count {merged_count} is smaller than baseline {existing_count}. "
                "Refusing to shrink master without --allow-shrink."
            )


def maybe_write_summary(path: Path | None, summary: dict) -> None:
    if not path:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    incoming_path = Path(args.incoming_json)
    master_csv = Path(args.master_csv)
    master_json = Path(args.master_json)
    backup_dir = Path(args.backup_dir)
    summary_path = Path(args.summary_json) if args.summary_json else None

    incoming_rows = dedupe_incoming(load_json_rows(incoming_path))
    master = load_master_rows(master_csv, master_json)
    baseline_rows = len(master.rows)
    existing_copy = [{field: row.get(field, "") for field in FIELDS} for row in master.rows]
    purged_existing_rows = 0
    if args.drop_rejected_existing:
        before = len(existing_copy)
        existing_copy = [row for row in existing_copy if is_accepted_row(row)]
        purged_existing_rows = before - len(existing_copy)
    merged_rows, merge_summary = merge_rows(existing_copy, incoming_rows)
    enforce_guards(master, merged_rows, args)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    csv_backup = backup_file(master_csv, backup_dir, timestamp)
    json_backup = backup_file(master_json, backup_dir, timestamp)

    atomic_write_csv(master_csv, merged_rows)
    atomic_write_json(master_json, merged_rows)

    summary = {
        "status": "ok",
        "master_source": master.source,
        "baseline_rows": baseline_rows,
        "purged_existing_rows": purged_existing_rows,
        "csv_backup": csv_backup,
        "json_backup": json_backup,
        **merge_summary,
        "master_csv": str(master_csv),
        "master_json": str(master_json),
        "incoming_json": str(incoming_path),
    }
    maybe_write_summary(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MergeGuardError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        raise SystemExit(2)
