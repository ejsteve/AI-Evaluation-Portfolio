import csv
from collections import Counter
from pathlib import Path


INPUT_FILE = Path(
    "Project-01-LLM-Response-Evaluation/data/clean_llm_evaluation.csv"
)


REQUIRED_FIELDS = [
    "id",
    "category",
    "prompt",
    "response_a",
    "response_b",

    "a_correctness",
    "b_correctness",

    "a_helpfulness",
    "b_helpfulness",

    "a_relevance",
    "b_relevance",

    "a_safety",
    "b_safety",

    "a_instruction_following",
    "b_instruction_following",

    "a_hallucination",
    "b_hallucination",

    "preference",
]


ALLOWED_VALUES = {
    "a_correctness": {
        "Correct",
        "Partially Correct",
        "Incorrect",
    },

    "b_correctness": {
        "Correct",
        "Partially Correct",
        "Incorrect",
    },

    "a_helpfulness": {
        "Very Helpful",
        "Helpful",
        "Somewhat Helpful",
        "Not Helpful",
    },

    "b_helpfulness": {
        "Very Helpful",
        "Helpful",
        "Somewhat Helpful",
        "Not Helpful",
    },

    "a_relevance": {
        "Directly Relevant",
        "Partially Relevant",
        "Irrelevant",
    },

    "b_relevance": {
        "Directly Relevant",
        "Partially Relevant",
        "Irrelevant",
    },

    "a_safety": {
        "Safe",
        "Potentially Unsafe",
        "Unsafe",
    },

    "b_safety": {
        "Safe",
        "Potentially Unsafe",
        "Unsafe",
    },

    "a_instruction_following": {
        "Fully Follows",
        "Partially Follows",
        "Does Not Follow",
    },

    "b_instruction_following": {
        "Fully Follows",
        "Partially Follows",
        "Does Not Follow",
    },

    "a_hallucination": {
        "No Unsupported Claim",
        "Minor Unsupported Claim",
        "Major Unsupported Claim",
    },

    "b_hallucination": {
        "No Unsupported Claim",
        "Minor Unsupported Claim",
        "Major Unsupported Claim",
    },

    "preference": {
        "Response A",
        "Response B",
        "Tie",
    },
}


def main():

    print("=" * 60)
    print("DATASET VALIDATION")
    print("=" * 60)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {INPUT_FILE}"
        )

    with INPUT_FILE.open(
        encoding="utf-8",
        newline=""
    ) as file:

        rows = list(csv.DictReader(file))

    errors = []

    # ---------------------------------------------------------
    # Check row count
    # ---------------------------------------------------------

    if len(rows) != 10:
        errors.append(
            f"Expected 10 rows but found {len(rows)}."
        )

    # ---------------------------------------------------------
    # Check columns
    # ---------------------------------------------------------

    actual_fields = set(rows[0].keys()) if rows else set()

    for field in REQUIRED_FIELDS:

        if field not in actual_fields:

            errors.append(
                f"Missing required column: {field}"
            )

    # ---------------------------------------------------------
    # Check duplicate IDs
    # ---------------------------------------------------------

    ids = [row["id"] for row in rows]

    duplicates = [
        item
        for item, count in Counter(ids).items()
        if count > 1
    ]

    if duplicates:

        errors.append(
            f"Duplicate IDs found: {duplicates}"
        )

    # ---------------------------------------------------------
    # Check required text fields
    # ---------------------------------------------------------

    text_fields = [
        "id",
        "category",
        "prompt",
        "response_a",
        "response_b",
    ]

    for row_number, row in enumerate(rows, start=1):

        for field in text_fields:

            if not row.get(field, "").strip():

                errors.append(
                    f"Row {row_number}: empty {field}"
                )

    # ---------------------------------------------------------
    # Check annotation values
    # ---------------------------------------------------------

    for row_number, row in enumerate(rows, start=1):

        for field, allowed in ALLOWED_VALUES.items():

            value = row.get(field, "").strip()

            if not value:

                errors.append(
                    f"Row {row_number}: missing {field}"
                )

            elif value not in allowed:

                errors.append(
                    f"Row {row_number}: invalid {field}={value!r}"
                )

    # ---------------------------------------------------------
    # Report
    # ---------------------------------------------------------

    print()
    print(f"Rows checked: {len(rows)}")

    if errors:

        print()
        print("VALIDATION FAILED")
        print("-" * 60)

        for error in errors:

            print(f"ERROR: {error}")

        raise SystemExit(1)

    print()
    print("VALIDATION PASSED")
    print("-" * 60)
    print("✓ Correct number of rows")
    print("✓ Required columns present")
    print("✓ No duplicate IDs")
    print("✓ Required text fields populated")
    print("✓ Annotation values match allowed labels")
    print("✓ Preference values are valid")

    print()
    print("Dataset is ready for statistical analysis.")


if __name__ == "__main__":
    main()
