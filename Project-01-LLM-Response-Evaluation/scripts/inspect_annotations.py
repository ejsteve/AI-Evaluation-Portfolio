import json
from pathlib import Path

INPUT_FILE = Path(
    "Project-01-LLM-Response-Evaluation/annotations/"
    "llm_evaluation_annotations.json"
)


def main():
    if not INPUT_FILE.exists():
        print(f"File not found: {INPUT_FILE}")
        return

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print("=" * 60)
    print("LLM EVALUATION ANNOTATION INSPECTION")
    print("=" * 60)

    print(f"Total exported tasks: {len(data)}")

    if not data:
        print("No data found.")
        return

    first_task = data[0]

    print("\nFirst task ID:")
    print(first_task.get("id"))

    print("\nData fields:")

    for key in first_task.get("data", {}):
        print(f" - {key}")

    annotations = first_task.get("annotations", [])

    print("\nNumber of annotations on first task:")
    print(len(annotations))

    if annotations:
        results = annotations[0].get("result", [])

        print("\nNumber of annotation results:")
        print(len(results))

        print("\nAnnotation result types:")

        for result in results:
            print(
                f" - from_name={result.get('from_name')}, "
                f"type={result.get('type')}"
            )


if __name__ == "__main__":
    main()
