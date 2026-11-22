# Dataset Card — Search Quality Evaluation

## 1. Dataset overview
- **Project:** Search Quality Evaluation
- **Dataset:** Search Relevance Demonstration Dataset
- **Format:** CSV
- **Records:** 20 query-result pairs
- **Unique queries:** 5
- **Language:** English
- **Data type:** Synthetic demonstration data
- **Annotation unit:** One search query paired with one result

## 2. Purpose
This dataset demonstrates how human evaluators can assess search-result relevance against user intent, including topical relevance, audience suitability, location, freshness, and navigational intent.

It is designed for portfolio demonstration and evaluator training, not production search ranking.

## 3. Dataset composition

| Query ID | Search intent | Records |
|---|---|---:|
| Q001 | Forgotten email password recovery | 4 |
| Q002 | Beginner Python tutorial | 4 |
| Q003 | Lagos weather forecast today | 4 |
| Q004 | Official passport renewal website | 4 |
| Q005 | Improving laptop battery life | 4 |
| **Total** | **Five query categories** | **20** |

## 4. Fields

| Field | Description |
|---|---|
| query_id | Unique query identifier |
| query | User's search query |
| result_id | Unique result identifier |
| result_title | Search-result title |
| result_snippet | Illustrative result description |
| relevance_grade | Human-assigned relevance grade from 0 to 3 |
| rationale | Explanation supporting the assigned grade |

## 5. Relevance scale

- **3 — Highly relevant:** Directly satisfies the user's primary intent.
- **2 — Relevant:** Useful and meaningfully related, but less complete or specific.
- **1 — Marginally relevant:** Related to the topic but provides limited help for the actual request.
- **0 — Irrelevant:** Does not meaningfully address the user's intent.

## 6. Label distribution

| Grade | Count | Percentage |
|---|---:|---:|
| 3 | 5 | 25% |
| 2 | 5 | 25% |
| 1 | 4 | 20% |
| 0 | 6 | 30% |
| **Total** | **20** | **100%** |

## 7. Data provenance
The query-result examples, titles, snippets, labels, and rationales were created as synthetic portfolio examples. They were not collected from a live search engine or real user search logs.

The relevance grades are demonstration annotations and have not been independently validated by a second annotator.

## 8. Intended uses
- Demonstrating search relevance annotation.
- Practising query-intent interpretation.
- Testing ranking evaluation scripts.
- Demonstrating Precision@K, NDCG@K, and Mean Reciprocal Rank.
- Identifying borderline relevance decisions and quality risks.
- Demonstrating dataset validation and documentation skills.

## 9. Out-of-scope uses
This dataset must not be presented as:
- A representative sample of real search-engine traffic.
- A benchmark of commercial search engines.
- Verified evidence of factual accuracy or website authenticity.
- An independently adjudicated relevance benchmark.
- Evidence of production search-system performance.

## 10. Quality controls
The project includes:
- Required-field and grade-range validation.
- Duplicate result-ID checks.
- Query-level ranking metrics.
- Ranking sensitivity testing.
- Written annotation guidelines.
- Error analysis and recommendations for independent review.

Automated validation checks dataset structure. It does not establish that human relevance labels are semantically correct.

## 11. Known limitations
- Only five queries and 20 synthetic examples.
- English-only examples.
- No live search-engine retrieval.
- No independent double annotation or inter-annotator agreement calculation.
- No verified source URLs.
- No independent factual, freshness, or website-authenticity checks.

## 12. Recommended future improvements
Expand the dataset, introduce independent annotators, adjudicate disagreements, record source URLs, include more query categories, and measure inter-annotator agreement before using the data for broader evaluation claims.
