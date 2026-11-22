# Ranking Sensitivity Test

## Objective
Test whether ranking metrics respond when search-result positions change.

## Method
The script reverses result order within each query in memory and recalculates Precision@3, NDCG@3 and Mean Reciprocal Rank. The source dataset is not modified.

## Results
| Metric | Original | Reversed |
|---|---:|---:|
| Precision@3 | 0.4000 | 0.3333 |
| NDCG@3 | 0.8411 | 0.3407 |
| MRR | 1.0000 | 0.9000 |

## Interpretation
The decrease in NDCG demonstrates that the evaluation responds to changes in result positions. This is a controlled test of the evaluation implementation, not a live search-engine benchmark.

## Limitations
The dataset is small and synthetic. This test does not independently verify the relevance labels.
