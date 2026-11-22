#!/usr/bin/env python3
"""Test whether ranking metrics respond to deliberately reversed rankings."""

import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "raw" / "search_relevance_dataset.csv"
K = 3
THRESHOLD = 2


def precision_at_k(grades):
    return sum(g >= THRESHOLD for g in grades[:K]) / K


def reciprocal_rank(grades):
    for rank, grade in enumerate(grades, start=1):
        if grade >= THRESHOLD:
            return 1 / rank
    return 0.0


def dcg_at_k(grades):
    return sum(
        (2 ** grade - 1) / math.log2(rank + 1)
        for rank, grade in enumerate(grades[:K], start=1)
    )


def ndcg_at_k(grades):
    ideal = sorted(grades, reverse=True)
    ideal_dcg = dcg_at_k(ideal)
    return dcg_at_k(grades) / ideal_dcg if ideal_dcg else 0.0


def calculate(groups):
    scores = []
    for query_id, rows in sorted(groups.items()):
        grades = [int(row["relevance_grade"]) for row in rows]
        scores.append({
            "query": query_id,
            "precision": precision_at_k(grades),
            "ndcg": ndcg_at_k(grades),
            "mrr": reciprocal_rank(grades),
        })

    return {
        metric: sum(item[metric] for item in scores) / len(scores)
        for metric in ("precision", "ndcg", "mrr")
    }


def main():
    groups = defaultdict(list)

    with DATASET.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            groups[row["query_id"]].append(row)

    original = calculate(groups)

    # Reverse each query's result order without modifying the source dataset.
    reversed_groups = {
        query_id: list(reversed(rows))
        for query_id, rows in groups.items()
    }
    reversed_scores = calculate(reversed_groups)

    print("RANKING SENSITIVITY TEST")
    print("Original ranking versus deliberately reversed ranking")
    print(f"{'Metric':<18}{'Original':>12}{'Reversed':>12}")
    print("-" * 42)

    for metric, label in (
        ("precision", "Precision@3"),
        ("ndcg", "NDCG@3"),
        ("mrr", "Mean RR"),
    ):
        print(
            f"{label:<18}"
            f"{original[metric]:>12.4f}"
            f"{reversed_scores[metric]:>12.4f}"
        )

    print("\nINTERPRETATION")
    for metric in ("precision", "ndcg", "mrr"):
        change = reversed_scores[metric] - original[metric]
        print(f"{metric}: change = {change:+.4f}")

    if reversed_scores["ndcg"] < original["ndcg"]:
        print("\nPASS: NDCG detects the deliberately reversed ranking.")
    else:
        print("\nREVIEW: NDCG did not decrease; inspect the dataset ordering.")

    print("Original dataset was not modified.")
    print("No existing evaluation results were overwritten.")


if __name__ == "__main__":
    main()
