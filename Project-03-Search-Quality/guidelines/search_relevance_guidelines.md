# Search Relevance Evaluation Guidelines

## 1. Purpose

These guidelines define a consistent method for rating how well a search result satisfies a user's query. They are designed for a small portfolio demonstration of search quality evaluation.

## 2. Unit of evaluation

Evaluate each query-result pair. Read the complete query and the available result title, snippet, and other supplied metadata before assigning a grade.

Do not assume that a result contains information that is not visible in the supplied evaluation record.

## 3. Relevance scale

| Grade | Label | Decision rule |
|---:|---|---|
| 3 | Highly relevant | Directly satisfies the main intent of the query with strong topical and intent alignment. |
| 2 | Relevant | Substantially helps satisfy the query but has a minor limitation in specificity, completeness, or alignment. |
| 1 | Marginally relevant | Has a meaningful connection to the query but only partially addresses the user's likely need. |
| 0 | Irrelevant | Does not meaningfully address the query, answers a different intent, or is unrelated. |

## 4. Rating workflow

1. Identify the likely user intent: informational, navigational, transactional, local, or another clearly supported intent.
2. Identify important entities, constraints, dates, locations, and requested actions.
3. Compare the result with the query's intent, not just shared keywords.
4. Consider whether the result appears specific and useful enough for the task.
5. Assign one relevance grade.
6. Record a concise rationale tied to evidence in the supplied result.

## 5. Special considerations

### Ambiguous queries
Use the available context. If multiple interpretations remain plausible, do not invent user intent. Record the ambiguity in the rationale and grade the result according to how well it fits the most supportable interpretation.

### Freshness
For queries that depend on current information, consider whether the result's stated date or freshness supports the need. Do not infer that a result is current when no evidence is provided.

### Factual accuracy
Relevance and factual accuracy are different dimensions. Rate relevance from the supplied evidence, and flag accuracy concerns separately when the evidence supports doing so. Do not claim that an unverified result is factually correct.

### Duplicate results
A duplicate may still be relevant to the query, but duplication can reduce the diversity and usefulness of a result list. Record duplication separately rather than automatically assigning grade 0.

### Missing information
Do not invent missing titles, snippets, dates, URLs, or context. If essential information is unavailable, document the limitation.

## 6. Rationale requirements

Each rating must include a short explanation that identifies the match or mismatch between query intent and result content. Avoid unsupported statements such as "this page is accurate" when no verification was performed.

## 7. Quality assurance

- Check that every grade is an integer from 0 through 3.
- Check that every evaluation has a query ID and result ID.
- Check for duplicate IDs and missing required fields.
- Review inconsistent ratings and unclear rationales.
- Distinguish automated structural validation from human judgment.
- Do not describe a small demonstration dataset as representative of all search users or search engines.

## 8. Limitations

These guidelines support a portfolio exercise. Results may depend on evaluator interpretation, incomplete snippets, and the composition of the sample. Independent double-rating and inter-annotator agreement should be added before making stronger reliability claims.
