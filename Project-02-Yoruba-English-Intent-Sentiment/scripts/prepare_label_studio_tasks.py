import csv
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_DIR / "data" / "raw" / "seed_examples.csv"
OUTPUT_FILE = PROJECT_DIR / "annotations" / "label_studio_tasks.json"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Source dataset not found: {INPUT_FILE}"
        )

    tasks = []

    with INPUT_FILE.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file)

        required = {"id", "text", "english_gloss"}
        missing = required - set(reader.fieldnames or [])

        if missing:
            raise ValueError(
                f"Missing required CSV columns: {sorted(missing)}"
            )

        for row in reader:
            tasks.append({
                "data": {
                    "source_id": row["id"],
                    "text": row["text"],
                    "english_gloss": row["english_gloss"],
                }
            })

    if not tasks:
        raise ValueError("The source CSV contains no tasks.")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

    print(f"Created: {OUTPUT_FILE}")
    print(f"Tasks prepared: {len(tasks)}")
    print("Fields:", list(tasks[0]["data"].keys()))
    print("Provisional intent and sentiment labels were not imported.")


if __name__ == "__main__":
    main()
