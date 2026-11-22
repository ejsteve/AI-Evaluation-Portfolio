# Case Study: Search Quality Evaluation

## Project summary
A practical demonstration of search-result relevance evaluation, dataset validation, ranking measurement and annotation error analysis.

**Dataset:** 20 synthetic query-result pairs across five queries.

## Methodology
1. Defined a four-level relevance scale from 0 (irrelevant) to 3 (highly relevant).
2. Organised five queries with four candidate results each.
3. Applied relevance labels and documented rationales.
4. Validated required fields, grade values, query coverage and duplicate result IDs.
5. Calculated Precision@3, NDCG@3 and Mean Reciprocal Rank.
6. Conducted a ranking sensitivity test by reversing result order in memory.
7. Reviewed borderline labels and documented limitations.

## Evaluation results
| Metric | Result |
|---|---:|
| Precision@3 | 0.4000 |
| NDCG@3 | 0.8411 |
| Mean Reciprocal Rank | 1.0000 |

These results reflect the supplied labels and illustrative CSV ordering only.

## Ranking sensitivity
| Metric | Original | Reversed |
|---|---:|---:|
| Precision@3 | 0.4000 | 0.3333 |
| NDCG@3 | 0.8411 | 0.3407 |
| Mean Reciprocal Rank | 1.0000 | 0.9000 |

## Error analysis
Review candidates include password-recovery intent, beginner accessibility, forecast freshness, official-site authenticity and operating-system-specific advice. These are potential review areas, not confirmed annotation errors. Independent double-rating and adjudication would be needed to assess consistency.

## Deliverables
- Synthetic search relevance dataset
- Relevance grading guidelines
- Dataset validation script
- Ranking evaluation and sensitivity scripts
- Per-query and aggregate metrics
- Error analysis and dataset documentation

## Skills demonstrated
Search relevance evaluation, data annotation, quality assurance, dataset validation, ranking metrics, sensitivity testing, error analysis and technical documentation.

## Limitations
The dataset is small and synthetic, not sourced from a live search engine. Labels have not been independently double-rated. Factual accuracy, freshness and website authenticity have not been independently verified.
