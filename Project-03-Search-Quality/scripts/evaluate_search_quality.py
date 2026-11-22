#!/usr/bin/env python3
"""Calculate ranking metrics for the Project 3 demonstration dataset."""

import csv
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "raw" / "search_relevance_dataset.csv"
RESULTS = ROOT / "results"
K = 3
RELEVANT_THRESHOLD = 2


def precision_at_k(grades, k):
    """Fraction of the top k results meeting the relevance threshold."""
    return sum(g >= RELEVANT_THRESHOLD for g in grades[:k]) / k


def reciprocal_rank(grades):
    """Reciprocal rank of the first relevant result; zero if none is found."""
    for rank, grade in enumerate(grades, start=1):
        if grade >= RELEVANT_THRESHOLD:
            return 1.0 / rank
    return 0.0


def dcg_at_k(grades, k):
    """Discounted cumulative gain using graded relevance."""
    return sum(
        (2 ** grade - 1) / math.log2(rank + 1)
        for rank, grade in enumerate(grades[:k], start=1)
    )


def ndcg_at_k(grades, k):
    """Normalized DCG against the ideal ordering of these same results."""
    ideal_grades = sorted(grades, reverse=True)
    ideal_dcg = dcg_at_k(ideal_grades, k)
    if ideal_dcg == 0:
        return 0.0
    return dcg_at_k(grades, k) / ideal_dcg


def main():
    if not DATASET.is_file():
        raise SystemExit(f"Dataset not found: {DATASET}")

    grouped = defaultdict(list)
    with DATASET.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            grouped[row["query_id"]].append(row)

    if not grouped:
        raise SystemExit("Dataset contains no query-result records.")

    query_metrics = []
    for query_id, rows in sorted(grouped.items()):
        # CSV row order is treated as the ranking order for this demonstration.
        grades = [int(row["relevance_grade"]) for row in rows]
        query_metrics.append({
            "query_id": query_id,
            "result_count": len(rows),
            f"precision_at_{K}": round(precision_at_k(grades, K), 4),
            f"ndcg_at_{K}": round(ndcg_at_k(grades, K), 4),
            "reciprocal_rank": round(reciprocal_rank(grades), 4),
        })

    metric_names = [f"precision_at_{K}", f"ndcg_at_{K}", "reciprocal_rank"]
    summary = {
        "dataset": "data/raw/search_relevance_dataset.csv",
        "query_count": len(query_metrics),
        "result_count": sum(item["result_count"] for item in query_metrics),
        "relevance_threshold": RELEVANT_THRESHOLD,
        "ranking_order": "CSV row order within each query",
        "metrics": {
            name: round(
                sum(item[name] for item in query_metrics) / len(query_metrics), 4
            )
            for name in metric_names
        },
        "limitations": [
            "Demonstration dataset with five queries; not representative of live search traffic.",
            "Row order is treated as ranking order and was not retrieved from a search engine.",
            "Relevance labels have not been independently double-rated.",
            "Metrics measure agreement with the supplied labels, not factual accuracy."
        ],
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    per_query_path = RESULTS / "query_metrics.csv"
    summary_path = RESULTS / "metrics_summary.json"

    with per_query_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=query_metrics[0].keys())
        writer.writeheader()
        writer.writerows(query_metrics)

    with summary_path.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
        handle.write("\n")

    print("SEARCH QUALITY EVALUATION")
    print(f"Queries evaluated: {summary['query_count']}")
    print(f"Result records: {summary['result_count']}")
    print(f"Relevant threshold: grade >= {RELEVANT_THRESHOLD}")
    print(f"Precision@{K}: {summary['metrics'][f'precision_at_{K}']:.4f}")
    print(f"NDCG@{K}: {summary['metrics'][f'ndcg_at_{K}']:.4f}")
    print(f"Mean Reciprocal Rank: {summary['metrics']['reciprocal_rank']:.4f}")
    print(f"\nPer-query results: {per_query_path.relative_to(ROOT)}")
    print(f"Summary JSON: {summary_path.relative_to(ROOT)}")
    print("\nLIMITATION: metrics reflect the supplied labels and CSV row order only.")


if __name__ == "__main__":
    main()
