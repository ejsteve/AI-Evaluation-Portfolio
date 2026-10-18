import csv
from collections import Counter
from pathlib import Path


INPUT_FILE = Path(
    "Project-01-LLM-Response-Evaluation/data/clean_llm_evaluation.csv"
)

OUTPUT_FILE = Path(
    "Project-01-LLM-Response-Evaluation/reports/evaluation_statistics.md"
)


DIMENSIONS = [
    ("Correctness", "a_correctness", "b_correctness"),
    ("Helpfulness", "a_helpfulness", "b_helpfulness"),
    ("Relevance", "a_relevance", "b_relevance"),
    ("Safety", "a_safety", "b_safety"),
    (
        "Instruction Following",
        "a_instruction_following",
        "b_instruction_following",
    ),
    (
        "Hallucination / Unsupported Claims",
        "a_hallucination",
        "b_hallucination",
    ),
]


def percentage(count, total):
    if total == 0:
        return 0

    return round(
        (count / total) * 100,
        1
    )


def distribution(rows, field):

    return Counter(
        row[field]
        for row in rows
        if row[field]
    )


def main():

    with INPUT_FILE.open(
        encoding="utf-8",
        newline=""
    ) as file:

        rows = list(csv.DictReader(file))

    total = len(rows)

    categories = Counter(
        row["category"]
        for row in rows
    )

    preferences = Counter(
        row["preference"]
        for row in rows
    )

    lines = []

    lines.append("# LLM Response Evaluation Statistics")
    lines.append("")
    lines.append("## Dataset Overview")
    lines.append("")
    lines.append(
        f"- Total evaluation examples: **{total}**"
    )
    lines.append(
        "- Evaluation format: Response A vs Response B"
    )
    lines.append(
        "- Annotation method: Human evaluation in Label Studio"
    )
    lines.append("")

    lines.append("## Task Categories")
    lines.append("")

    for category, count in categories.items():

        lines.append(
            f"- **{category}**: {count} "
            f"({percentage(count, total)}%)"
        )

    lines.append("")

    lines.append("## Overall Preference")
    lines.append("")

    for preference in [
        "Response A",
        "Response B",
        "Tie",
    ]:

        count = preferences.get(
            preference,
            0
        )

        lines.append(
            f"- **{preference}**: {count} "
            f"({percentage(count, total)}%)"
        )

    lines.append("")

    lines.append("## Response Quality Dimensions")
    lines.append("")

    for label, a_field, b_field in DIMENSIONS:

        lines.append(
            f"### {label}"
        )

        lines.append("")

        a_distribution = distribution(
            rows,
            a_field
        )

        b_distribution = distribution(
            rows,
            b_field
        )

        lines.append("#### Response A")

        for value, count in a_distribution.items():

            lines.append(
                f"- {value}: {count} "
                f"({percentage(count, total)}%)"
            )

        lines.append("")

        lines.append("#### Response B")

        for value, count in b_distribution.items():

            lines.append(
                f"- {value}: {count} "
                f"({percentage(count, total)}%)"
            )

        lines.append("")

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print("=" * 60)
    print("STATISTICS GENERATED")
    print("=" * 60)
    print(f"Examples analyzed: {total}")
    print(f"Report: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
