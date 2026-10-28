# Quality Assurance Plan — Yoruba-English Intent and Sentiment Dataset

## 1. Purpose

This document describes the quality assurance process used for the
Yoruba-English Intent and Sentiment Annotation project.

The goal is to demonstrate repeatable dataset checks, annotation review,
traceability, and responsible reporting of limitations.

## 2. Dataset Scope

- Dataset size at this stage: 20 examples.
- Data source: synthetic examples created for portfolio practice.
- Annotation interface: Label Studio.
- Export format: Label Studio JSON.
- Processed formats: CSV and JSONL.
- Primary labels: language, intent, and sentiment.
- Additional review fields: English gloss quality and reviewer notes.

These examples are not authentic customer conversations and should not be
represented as a production or representative Yoruba-language dataset.

## 3. Quality Assurance Workflow

1. Generate the synthetic seed examples.
2. Check the seed dataset for required columns, missing values, duplicate
   identifiers, and allowed label values.
3. Prepare annotation tasks for Label Studio without exposing provisional
   labels unnecessarily.
4. Review each task in Label Studio and record the selected labels and notes.
5. Export the completed annotations in JSON format.
6. Preserve the export in annotations/label_studio_export.json.
7. Run scripts/clean_label_studio_export.py to create the processed CSV,
   JSONL, and quality report.
8. Compare important corrected labels in the raw export and processed CSV.
9. Review uncertain Yoruba text, English glosses, intent, and sentiment with
   a competent Yoruba speaker before claiming linguistic validation.

## 4. Automated Checks

The current cleaning workflow reports checks for:

- Required annotation fields.
- Allowed label values.
- Completed annotations.
- Duplicate source identifiers.
- Structural consistency of exported records.
- Presence of required values.

Latest recorded run:

- Tasks read: 20.
- Rows written: 20.
- Rows passing automated checks: 20.
- Rows needing review according to automated checks: 0.
- Duplicate source IDs: 0.

These results describe the automated checks implemented by the current
script. They do not establish that every annotation is semantically correct.

## 5. Human Review Checklist

A reviewer should check each record for:

- Correct language classification, including meaningful code-switching.
- Intent that reflects the main communicative purpose.
- Sentiment supported by the wording rather than assumptions.
- English gloss that accurately preserves the source meaning.
- Preservation of Yoruba tone marks and other original characters.
- Review notes that describe the actual text and its uncertainty.
- Appropriate handling of ambiguous or context-dependent expressions.

A competent Yoruba speaker should review the Yoruba examples and their
English glosses before the dataset is described as linguistically validated.

## 6. Disagreement and Adjudication

When reviewers disagree:

1. Identify the record and disputed field.
2. Record the competing interpretations.
3. Explain the linguistic or contextual evidence for each interpretation.
4. Request review from a competent Yoruba speaker where appropriate.
5. Record the final decision and its rationale.
6. Update the annotation and regenerate the processed dataset.

Do not claim inter-annotator agreement unless multiple independent
annotations have been collected and analyzed using a documented method.

## 7. Versioning and Traceability

- Keep the original Label Studio export.
- Use the processed CSV and JSONL as derived outputs, not as replacements
  for the raw export.
- Regenerate processed outputs after changes to annotations.
- Keep the quality report aligned with the latest cleaning run.
- Record meaningful changes to labels and annotation guidelines.
- Do not silently overwrite important source data without a backup.

## 8. Current Limitations

The dataset contains only 20 synthetic examples. Automated validation
checks structure and allowed values, not linguistic correctness.

No claim of representative sampling, production readiness, independent
reviewer agreement, or measured model performance is made.

Further review and expansion are required before using the dataset to
evaluate real-world Yoruba-language systems or draw broad conclusions.
