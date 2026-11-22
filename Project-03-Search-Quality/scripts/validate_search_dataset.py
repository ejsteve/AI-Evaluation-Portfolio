#!/usr/bin/env python3
"""Validate the structure and labels of the search relevance dataset."""

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "raw" / "search_relevance_dataset.csv"

REQUIRED_COLUMNS = {
    "query_id",
    "query",
    "result_id",
    "result_title",
    "result_snippet",
    "relevance_grade",
    "rationale",
}
VALID_GRADES = {"0", "1", "2", "3"}


def main():
    if not DATASET.is_file():
        print(f"VALIDATION: FAILED — dataset not found: {DATASET}")
        return 1

    with DATASET.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        rows = list(reader)

    errors = []

    if columns != REQUIRED_COLUMNS:
        errors.append(
            f"Column mismatch. Missing: {sorted(REQUIRED_COLUMNS - columns)}; "
            f"unexpected: {sorted(columns - REQUIRED_COLUMNS)}"
        )

    if not rows:
        errors.append("Dataset contains no data rows.")

    result_ids = []
    query_counts = Counter()
    grade_counts = Counter()

    for line_number, row in enumerate(rows, start=2):
        for field in REQUIRED_COLUMNS:
            if not (row.get(field) or "").strip():
                errors.append(f"Line {line_number}: missing value for '{field}'.")

        query_id = (row.get("query_id") or "").strip()
        result_id = (row.get("result_id") or "").strip()
        grade = (row.get("relevance_grade") or "").strip()

        if query_id:
            query_counts[query_id] += 1

        if result_id:
            result_ids.append(result_id)

        if grade not in VALID_GRADES:
            errors.append(
                f"Line {line_number}: invalid relevance grade '{grade}'. "
                "Expected 0, 1, 2, or 3."
            )
        else:
            grade_counts[grade] += 1

    duplicates = sorted(
        result_id for result_id, count in Counter(result_ids).items()
        if count > 1
    )
    if duplicates:
        errors.append(f"Duplicate result_id values: {duplicates}")

    print(f"Dataset: {DATASET.relative_to(ROOT)}")
    print(f"Rows: {len(rows)}")
    print(f"Unique queries: {len(query_counts)}")
    print(f"Rows per query: {dict(sorted(query_counts.items()))}")
    print(f"Grade distribution: {dict(sorted(grade_counts.items()))}")

    if errors:
        print("\nVALIDATION: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nVALIDATION: PASSED")
    print("Note: structural validation does not certify semantic rating accuracy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
