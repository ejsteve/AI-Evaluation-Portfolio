import csv
import json
from pathlib import Path


INPUT_FILE = Path(
    "Project-01-LLM-Response-Evaluation/annotations/llm_evaluation_annotations.json"
)

OUTPUT_DIR = Path("Project-01-LLM-Response-Evaluation/data")

OUTPUT_JSONL = OUTPUT_DIR / "clean_llm_evaluation.jsonl"
OUTPUT_CSV = OUTPUT_DIR / "clean_llm_evaluation.csv"


FIELDS = [
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

    "evaluator_notes",
]


def extract_value(result):
    """
    Extract the actual annotation value from a Label Studio result.
    Supports Choices and TextArea fields.
    """

    value = result.get("value", {})

    # Label Studio Choices
    if "choices" in value:
        choices = value.get("choices") or []

        if choices:
            return choices[0]

        return ""

    # Label Studio TextArea
    if "text" in value:
        text = value.get("text")

        if isinstance(text, list):
            return " ".join(str(x) for x in text)

        if text is None:
            return ""

        return str(text)

    return ""


def main():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    print("=" * 60)
    print("LLM EVALUATION DATA CLEANER")
    print("=" * 60)

    tasks = json.loads(
        INPUT_FILE.read_text(encoding="utf-8")
    )

    if not isinstance(tasks, list):
        raise ValueError(
            "Expected Label Studio export to be a JSON list."
        )

    print(f"Raw Label Studio tasks: {len(tasks)}")

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    rows = []

    for task in tasks:

        data = task.get("data", {})

        row = {
            field: ""
            for field in FIELDS
        }

        # Original task information
        row["id"] = task.get("id", "")
        row["category"] = data.get("category", "")
        row["prompt"] = data.get("prompt", "")
        row["response_a"] = data.get("response_a", "")
        row["response_b"] = data.get("response_b", "")

        # Annotation information
        annotations = task.get("annotations", [])

        if annotations:

            # We expect one completed annotation per task.
            annotation = annotations[0]

            results = annotation.get("result", [])

            for result in results:

                field_name = result.get("from_name")

                if field_name in row:

                    row[field_name] = extract_value(result)

        rows.append(row)

    # ---------------------------------------------------------
    # Write JSONL
    # ---------------------------------------------------------

    with OUTPUT_JSONL.open(
        "w",
        encoding="utf-8"
    ) as file:

        for row in rows:

            file.write(
                json.dumps(
                    row,
                    ensure_ascii=False
                )
                + "\n"
            )

    # ---------------------------------------------------------
    # Write CSV
    # ---------------------------------------------------------

    with OUTPUT_CSV.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDS
        )

        writer.writeheader()

        writer.writerows(rows)

    print()
    print("=" * 60)
    print("CLEANING COMPLETE")
    print("=" * 60)

    print(f"Rows processed: {len(rows)}")
    print(f"JSONL created:  {OUTPUT_JSONL}")
    print(f"CSV created:    {OUTPUT_CSV}")

    print()
    print("Columns:")
    for field in FIELDS:
        print(f"  - {field}")


if __name__ == "__main__":
    main()
