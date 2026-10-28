# Dataset Card: Yoruba-English Intent and Sentiment Dataset

## 1. Dataset Overview

This dataset is a small, synthetic collection of English, Yoruba, and
code-switched text examples prepared to demonstrate an AI data annotation
and quality assurance workflow.

The project covers language identification, intent classification,
sentiment classification, English gloss review, annotation notes, and
automated structural validation.

**Dataset status:** Provisional portfolio dataset; linguistic review
remains outstanding.

## 2. Intended Uses

Potential educational and portfolio uses include:

- Demonstrating a Label Studio annotation workflow.
- Practising intent and sentiment annotation.
- Demonstrating dataset cleaning and structural validation.
- Exploring quality assurance for multilingual and code-switched text.
- Demonstrating CSV and JSONL data preparation.
- Building reproducible data annotation project documentation.

The dataset is not intended to establish the accuracy of a production
model or the performance of a system across Yoruba-speaking populations.

## 3. Dataset Composition

The current processed dataset contains 20 examples.

### Language distribution

| Language category | Number of records |
|---|---:|
| English | 7 |
| Yoruba | 10 |
| Code-switched | 3 |
| Total | 20 |

### Sentiment distribution

| Sentiment | Number of records |
|---|---:|
| Neutral | 7 |
| Negative | 5 |
| Mixed | 5 |
| Positive | 3 |
| Total | 20 |

The dataset includes intent labels such as order status, complaints,
order cancellation, appreciation, product feedback, service feedback,
account access, payment issues, refund requests, and technical support.

These counts describe the current processed dataset and may change when
annotations are reviewed or updated.

## 4. Data Creation and Processing

The examples were synthetically created for portfolio practice. They
are not collected from real customers.

The workflow includes:

1. Generating seed examples.
2. Validating the seed dataset.
3. Preparing annotation tasks for Label Studio.
4. Reviewing and annotating the tasks.
5. Exporting annotations in Label Studio JSON format.
6. Cleaning the exported annotations into CSV and JSONL.
7. Producing a structural quality report.

### Current output files

- `data/raw/seed_examples.csv`
- `annotations/label_studio_tasks.json`
- `annotations/label_studio_export.json`
- `data/processed/yoruba_english_annotated.csv`
- `data/processed/yoruba_english_annotated.jsonl`
- `reports/project2_quality_report.txt`

## 5. Annotation Fields

The dataset includes:

- `source_id`: Identifier for the original example.
- `text`: Original message.
- `english_gloss`: English translation or explanation.
- `language`: English, Yoruba, or code-switched.
- `intent`: Primary communicative goal.
- `sentiment`: Positive, neutral, negative, or mixed.
- `gloss_quality`: Reviewer assessment of the English gloss.
- `review_notes`: Notes about interpretation or uncertainty.
- `annotation_status`: Processing status.
- `validation_issues`: Issues reported by the automated checks.

The processed schema reflects the current cleaning script. Consult the
actual CSV header before relying on these fields in downstream tools.

## 6. Quality Assurance Results

The latest recorded automated validation run reported:

- 20 tasks read.
- 20 rows written.
- 20 rows passing automated checks.
- Zero duplicate source IDs.
- Zero rows flagged by the script's automated validation.

These checks cover structural consistency, required fields, and allowed
labels. They do not prove that the language labels, intent, sentiment,
or English glosses are semantically correct.

## 7. Language Review and Limitations

Yoruba wording, tone marks, context-dependent meanings, code-switching,
and English glosses require review by a competent Yoruba speaker.

The examples are synthetic and the dataset is small. It does not
represent the full diversity of Yoruba dialects, writing conventions,
speakers, or real-world customer conversations.

The current dataset should not be described as linguistically validated.
No independent inter-annotator agreement or model-performance results
are claimed.

## 8. Ethical and Privacy Considerations

Because the examples were created synthetically, the dataset is intended
to avoid representing them as genuine customer records. The project
should continue to exclude personal or confidential information.

Users should not assume that results obtained from this small dataset
generalize to real people or operational systems.

## 9. Recommended Review Before Broader Use

Before using this dataset for model evaluation or publishing claims about
Yoruba-language performance:

1. Obtain competent Yoruba-speaker review of the source text and glosses.
2. Resolve uncertain language, intent, and sentiment labels.
3. Document meaningful annotation changes.
4. Expand the dataset with a clearly described sampling strategy.
5. Consider independent annotations and an appropriate agreement measure.
6. Rerun validation and update the dataset statistics.
7. Keep synthetic examples clearly distinguished from authentic data.

## 10. License and Publication Status

Choose and document an appropriate license before public distribution.
Do not imply that a license has been selected until that decision has
actually been made.

This dataset card describes the current portfolio version and should be
updated whenever the dataset or annotation process changes.
