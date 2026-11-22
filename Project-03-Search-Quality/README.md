# Project 03 — Search Quality Evaluation

**Category:** AI Data Evaluation, Search Relevance and Quality Assurance

## Overview
A practical demonstration of search-result relevance evaluation, dataset validation, ranking metrics and annotation error analysis.

The dataset contains 20 synthetic query-result pairs across five queries. It is not a live search-engine benchmark.

## Relevance scale
| Grade | Meaning |
|---|---|
| 3 | Highly relevant |
| 2 | Relevant |
| 1 | Marginally relevant |
| 0 | Irrelevant |

## Evaluation results
| Metric | Result |
|---|---:|
| Precision@3 | 0.4000 |
| NDCG@3 | 0.8411 |
| Mean Reciprocal Rank | 1.0000 |

## Ranking sensitivity test
| Metric | Original | Reversed |
|---|---:|---:|
| Precision@3 | 0.4000 | 0.3333 |
| NDCG@3 | 0.8411 | 0.3407 |
| MRR | 1.0000 | 0.9000 |

## Reproduce
Run from the repository root:

    python Project-03-Search-Quality/scripts/validate_search_dataset.py
    python Project-03-Search-Quality/scripts/evaluate_search_quality.py
    python Project-03-Search-Quality/scripts/test_ranking_sensitivity.py

## Project contents
- data/raw/ — synthetic relevance dataset
- guidelines/ — grading guidelines
- scripts/ — validation and evaluation scripts
- results/ — evaluation metrics
- reports/ — error analysis and sensitivity report
- case-study/ — portfolio case study
- DATASET_CARD.md — dataset description and limitations

## Skills demonstrated
Search relevance annotation, relevance grading, data quality assurance, dataset validation, Precision@K, NDCG@K, Mean Reciprocal Rank, ranking sensitivity analysis, error analysis and technical documentation.

## Limitations
This small synthetic dataset is not representative of live search traffic. Labels have not been independently double-rated. Ranking order is illustrative, and factual accuracy, freshness and website authenticity have not been independently verified.
