import csv
import json
from pathlib import Path
from collections import Counter

INPUT_FILE = Path("annotations/label_studio_export.json")
OUTPUT_DIR = Path("data/processed")
CSV_FILE = OUTPUT_DIR / "yoruba_english_annotated.csv"
JSONL_FILE = OUTPUT_DIR / "yoruba_english_annotated.jsonl"
REPORT_FILE = Path("reports/project2_quality_report.txt")

ALLOWED_LABELS = {
    "language": {"English", "Yoruba", "code_switched"},
    "intent": {
        "order_status", "payment_issue", "refund_request",
        "order_cancellation", "account_access", "technical_support",
        "product_inquiry", "product_feedback", "delivery_issue",
        "price_inquiry", "appreciation", "complaint",
        "service_feedback", "request_help", "general_inquiry", "other"
    },
    "sentiment": {"positive", "neutral", "negative", "mixed"},
    "gloss_quality": {"accurate", "needs_review", "uncertain"},
}

DATA_FIELDS = [
    "source_id", "text", "english_gloss", "language", "intent",
    "sentiment", "gloss_quality", "review_notes"
]

REVIEW_FIELDS = [
    "linguistic_review_status",
    "linguistic_reviewer",
    "linguistic_review_date",
]

OUTPUT_FIELDS = DATA_FIELDS + [
    "annotation_status",
    "validation_issues",
] + REVIEW_FIELDS


def extract_result(result_items):
    """Convert Label Studio result entries into simple field values."""
    extracted = {}

    for item in result_items or []:
        field = item.get("from_name")
        value = item.get("value", {})

        if not field:
            continue

        if "choices" in value:
            extracted[field] = value["choices"][0] if value["choices"] else ""
        elif "text" in value:
            extracted[field] = " ".join(value["text"]).strip()

    return extracted


def choose_annotation(task):
    """Use the latest completed, non-cancelled annotation if several exist."""
    annotations = [
        annotation
        for annotation in task.get("annotations", [])
        if not annotation.get("was_cancelled", False)
        and annotation.get("result") is not None
    ]

    if not annotations:
        return None, 0

    annotations.sort(
        key=lambda a: a.get("updated_at") or a.get("created_at") or ""
    )
    return annotations[-1], len(annotations)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {INPUT_FILE}. Check that you are in the Project 2 directory."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Expected the Label Studio export to be a JSON list.")

    # Load prior processed records so human review metadata and
    # reviewer-added notes survive a future rebuild.
    previous_rows = {}
    if CSV_FILE.exists():
        with CSV_FILE.open(
            "r", newline="", encoding="utf-8-sig"
        ) as previous_file:
            for previous_row in csv.DictReader(previous_file):
                source_id = previous_row.get("source_id", "").strip()
                if source_id:
                    previous_rows[source_id] = previous_row

    rows = []
    issues_count = Counter()
    intent_counts = Counter()
    sentiment_counts = Counter()
    language_counts = Counter()
    annotated_tasks = 0
    unannotated_tasks = 0
    multiple_annotation_tasks = 0

    for task in tasks:
        source_data = task.get("data") or {}
        annotation, annotation_count = choose_annotation(task)

        if annotation_count > 1:
            multiple_annotation_tasks += 1

        labels = extract_result(annotation.get("result", [])) if annotation else {}

        if annotation:
            annotated_tasks += 1
        else:
            unannotated_tasks += 1

        row = {
            "source_id": source_data.get("source_id", ""),
            "text": source_data.get("text", ""),
            "english_gloss": source_data.get("english_gloss", ""),
            "language": labels.get("language", ""),
            "intent": labels.get("intent", ""),
            "sentiment": labels.get("sentiment", ""),
            "gloss_quality": labels.get("gloss_quality", ""),
            "review_notes": labels.get("review_notes", ""),
        }

        # Preserve human review metadata only when the reviewed text and
        # English gloss are unchanged.
        previous = previous_rows.get(row["source_id"], {})
        same_reviewed_content = (
            previous.get("text", "") == row["text"]
            and previous.get("english_gloss", "") == row["english_gloss"]
        )
        review_status = (
            previous.get("linguistic_review_status", "").strip()
            if same_reviewed_content
            else ""
        )

        for field in REVIEW_FIELDS:
            row[field] = previous.get(field, "") if review_status else ""

        # Keep reviewer-added notes only when the reviewed content is unchanged.
        if review_status and previous.get("review_notes", "").strip():
            row["review_notes"] = previous["review_notes"]

        problems = []

        for field in ("source_id", "text", "english_gloss"):
            if not str(row[field]).strip():
                problems.append(f"missing_{field}")

        for field, allowed_values in ALLOWED_LABELS.items():
            value = row[field]
            if not value:
                problems.append(f"missing_{field}")
            elif value not in allowed_values:
                problems.append(f"invalid_{field}:{value}")

        if not annotation:
            problems.append("no_completed_annotation")

        if not row["review_notes"].strip():
            problems.append("missing_review_notes")

        row["annotation_status"] = (
            "needs_review" if problems else "validated"
        )
        row["validation_issues"] = "; ".join(problems)

        for problem in problems:
            issues_count[problem] += 1

        if row["intent"]:
            intent_counts[row["intent"]] += 1
        if row["sentiment"]:
            sentiment_counts[row["sentiment"]] += 1
        if row["language"]:
            language_counts[row["language"]] += 1

        rows.append(row)

    # Check duplicate source IDs.
    source_ids = [
        row["source_id"] for row in rows if row["source_id"].strip()
    ]
    duplicate_ids = [
        source_id
        for source_id, count in Counter(source_ids).items()
        if count > 1
    ]

    # Save CSV.
    with CSV_FILE.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    # Save JSON Lines, one record per line.
    with JSONL_FILE.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")

    validated_count = sum(
        row["annotation_status"] == "validated" for row in rows
    )
    needs_review_count = len(rows) - validated_count

    report_lines = [
        "PROJECT 2 — LABEL STUDIO DATA QUALITY REPORT",
        "=" * 48,
        f"Input file: {INPUT_FILE}",
        f"Tasks exported: {len(tasks)}",
        f"Tasks with completed annotations: {annotated_tasks}",
        f"Tasks without completed annotations: {unannotated_tasks}",
        f"Tasks with multiple annotations: {multiple_annotation_tasks}",
        f"Rows written: {len(rows)}",
        f"Rows passing automated checks: {validated_count}",
        f"Rows needing review: {needs_review_count}",
        f"Duplicate source IDs: {duplicate_ids if duplicate_ids else 'None found'}",
        "",
        "LANGUAGE COUNTS",
        "-" * 20,
    ]

    report_lines.extend(
        f"{label}: {count}" for label, count in sorted(language_counts.items())
    )
    report_lines.extend(["", "INTENT COUNTS", "-" * 20])
    report_lines.extend(
        f"{label}: {count}" for label, count in sorted(intent_counts.items())
    )
    report_lines.extend(["", "SENTIMENT COUNTS", "-" * 20])
    report_lines.extend(
        f"{label}: {count}" for label, count in sorted(sentiment_counts.items())
    )
    report_lines.extend(["", "VALIDATION ISSUE COUNTS", "-" * 28])
    report_lines.extend(
        f"{issue}: {count}" for issue, count in sorted(issues_count.items())
    )

    if duplicate_ids:
        report_lines.append(
            "WARNING: Duplicate source IDs must be investigated."
        )

    report_lines.extend([
        "",
        "IMPORTANT LIMITATION",
        "-" * 20,
        "Automated checks verify structure, required fields, and allowed labels.",
        "They do not prove that Yoruba wording, English glosses, intent, or",
        "sentiment are linguistically or semantically correct.",
        "A project-owner linguistic review is documented for Yoruba and",
        "code-switched wording and English glosses in 12 records.",
        "Seven English-only records were not reviewed in that pass.",
        "Intent and sentiment labels have not been independently certified.",
        "See reports/human_linguistic_review_report.txt for scope and limits.",
    ])

    REPORT_FILE.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print("Cleaning and validation complete.")
    print(f"Tasks read: {len(tasks)}")
    print(f"Rows passing automated checks: {validated_count}")
    print(f"Rows needing review: {needs_review_count}")
    print(f"Duplicate source IDs: {len(duplicate_ids)}")
    print(f"CSV: {CSV_FILE}")
    print(f"JSONL: {JSONL_FILE}")
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
