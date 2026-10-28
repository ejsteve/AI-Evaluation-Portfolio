
import csv
import sys
from collections import Counter
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_DIR / "data" / "raw" / "seed_examples.csv"

ALLOWED_LANGUAGES = {
    "English",
    "Yoruba",
    "code_switched",
}

ALLOWED_INTENTS = {
    "order_status",
    "payment_issue",
    "refund_request",
    "order_cancellation",
    "account_access",
    "technical_support",
    "product_inquiry",
    "product_feedback",
    "delivery_issue",
    "price_inquiry",
    "appreciation",
    "complaint",
    "service_feedback",
    "request_help",
    "general_inquiry",
    "other",
}

ALLOWED_SENTIMENTS = {
    "positive",
    "neutral",
    "negative",
    "mixed",
}

REQUIRED_COLUMNS = {
    "id",
    "text",
    "language",
    "intent",
    "sentiment",
    "english_gloss",
}


def main():
    errors = []

    if not INPUT_FILE.exists():
        print(f"ERROR: Dataset not found: {INPUT_FILE}")
        return 1

    try:
        with INPUT_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            columns = set(reader.fieldnames or [])
            missing_columns = REQUIRED_COLUMNS - columns

            if missing_columns:
                errors.append(
                    f"Missing required columns: {sorted(missing_columns)}"
                )

            rows = list(reader)

    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: Could not read dataset: {exc}")
        return 1

    if not rows:
        errors.append("Dataset contains no data rows.")

    ids = [row.get("id", "").strip() for row in rows]
    id_counts = Counter(ids)

    if any(not record_id for record_id in ids):
        errors.append("One or more records have an empty ID.")

    duplicate_ids = sorted(
        record_id
        for record_id, count in id_counts.items()
        if record_id and count > 1
    )

    if duplicate_ids:
        errors.append(f"Duplicate IDs found: {duplicate_ids}")

    for line_number, row in enumerate(rows, start=2):
        record_id = row.get("id", "").strip() or f"line {line_number}"

        for field in ("text", "language", "intent", "sentiment", "english_gloss"):
            if not row.get(field, "").strip():
                errors.append(f"{record_id}: empty required field '{field}'")

        language = row.get("language", "").strip()
        intent = row.get("intent", "").strip()
        sentiment = row.get("sentiment", "").strip()

        if language and language not in ALLOWED_LANGUAGES:
            errors.append(f"{record_id}: invalid language '{language}'")

        if intent and intent not in ALLOWED_INTENTS:
            errors.append(f"{record_id}: invalid intent '{intent}'")

        if sentiment and sentiment not in ALLOWED_SENTIMENTS:
            errors.append(f"{record_id}: invalid sentiment '{sentiment}'")

    print("Dataset:", INPUT_FILE)
    print("Total rows:", len(rows))
    print("Unique IDs:", len(set(ids)))
    print("Language distribution:", dict(Counter(
        row.get("language", "").strip() for row in rows
    )))
    print("Intent distribution:", dict(Counter(
        row.get("intent", "").strip() for row in rows
    )))
    print("Sentiment distribution:", dict(Counter(
        row.get("sentiment", "").strip() for row in rows
    )))

    if errors:
        print(f"\nVALIDATION FAILED: {len(errors)} issue(s)")
        for error in errors:
            print("-", error)
        return 1

    print("\nVALIDATION PASSED")
    print("Structural and allowed-label checks passed.")
    print("Note: translation accuracy and semantic correctness require human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
