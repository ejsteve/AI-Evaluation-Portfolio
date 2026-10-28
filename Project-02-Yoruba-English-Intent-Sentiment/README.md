# Yoruba-English Intent and Sentiment Annotation

A portfolio project demonstrating multilingual data annotation, intent
classification, sentiment classification, dataset cleaning, and quality
assurance using Label Studio and Python.

## Project Status

**Status:** Provisional portfolio dataset.

- 20 synthetic examples processed.
- 20 rows passed the current automated structural checks.
- Zero duplicate source IDs were reported.
- Yoruba-speaker review remains outstanding.
- No model-performance or inter-annotator agreement claims are made.

## Project Objectives

This project demonstrates how to:

1. Prepare a small multilingual dataset.
2. Define consistent annotation labels and decision rules.
3. Configure a Label Studio annotation interface.
4. Annotate English, Yoruba, and code-switched messages.
5. Export annotations as JSON.
6. Clean annotations into CSV and JSONL.
7. Validate dataset structure and allowed labels.
8. Document quality checks, uncertainty, and limitations.

## Dataset Overview

The dataset contains 20 synthetic examples created for portfolio practice.
They are not authentic customer conversations.

### Language distribution

| Language | Records |
|---|---:|
| English | 7 |
| Yoruba | 10 |
| Code-switched | 3 |
| Total | 20 |

### Sentiment distribution

| Sentiment | Records |
|---|---:|
| Neutral | 7 |
| Negative | 5 |
| Mixed | 5 |
| Positive | 3 |
| Total | 20 |

The intent taxonomy includes order status, payment issues, refunds,
cancellations, account access, technical support, product inquiries,
product feedback, delivery issues, price inquiries, appreciation,
complaints, service feedback, help requests, and general inquiries.

Counts describe the current annotation version and may change after review.

## Technology

- Python
- CSV and JSONL
- Label Studio
- Git and GitHub

## Repository Structure

```text
Project-02-Yoruba-English-Intent-Sentiment/
├── annotations/
│   ├── label_studio_export.json
│   ├── label_studio_export_backup.json
│   └── label_studio_tasks.json
├── data/
│   ├── raw/
│   │   └── seed_examples.csv
│   └── processed/
│       ├── yoruba_english_annotated.csv
│       └── yoruba_english_annotated.jsonl
├── guidelines/
│   ├── annotation_guidelines.md
│   ├── label_studio_config.xml
│   └── quality_assurance.md
├── reports/
│   ├── dataset_card.md
│   └── project2_quality_report.txt
├── scripts/
│   ├── generate_seed_dataset.py
│   ├── validate_seed_dataset.py
│   ├── prepare_label_studio_tasks.py
│   └── clean_label_studio_export.py
└── README.md
```

## Setup

Run commands from this project directory.

If you are using the existing project virtual environment, activate it
from the portfolio root before entering this directory.

Confirm that Python is available:

```bash
python --version
```

The scripts use Python's standard library for their documented data
processing operations. Label Studio is used for interactive annotation.

## Reproduce the Workflow

### 1. Generate the seed dataset

```bash
python scripts/generate_seed_dataset.py
```

This generates the seed examples in `data/raw/seed_examples.csv`.

### 2. Validate the seed dataset

```bash
python scripts/validate_seed_dataset.py
```

Review the command output and resolve any validation errors before proceeding.

### 3. Prepare Label Studio tasks

```bash
python scripts/prepare_label_studio_tasks.py
```

This prepares the tasks in `annotations/label_studio_tasks.json`.

### 4. Annotate in Label Studio

Import the prepared tasks into a Label Studio project configured with
`guidelines/label_studio_config.xml`.

Review language, intent, sentiment, and English gloss quality. Record
uncertainties in reviewer notes. Save the annotations and export the
completed tasks as JSON.

Place the current export at:

`annotations/label_studio_export.json`

Back up an existing export before replacing it.

### 5. Clean the exported annotations

```bash
python scripts/clean_label_studio_export.py
```

This generates:

- `data/processed/yoruba_english_annotated.csv`
- `data/processed/yoruba_english_annotated.jsonl`
- `reports/project2_quality_report.txt`

### 6. Check the processed dataset

```bash
python -c "import csv; p='data/processed/yoruba_english_annotated.csv'; f=open(p,encoding='utf-8-sig',newline=''); r=csv.DictReader(f); rows=list(r); print('Rows:',len(rows)); print('Columns:',r.fieldnames); f.close()"
```

The expected row count for the current version is 20.

Always rerun the cleaning script after changing annotations. Review the
quality report and verify that important changes appear in the processed
outputs.

## Quality Assurance

The current automated checks report:

- 20 tasks read.
- 20 rows written.
- 20 rows passing the implemented automated checks.
- Zero duplicate source IDs.
- Zero rows flagged by the script's current structural validation.

These checks do not prove that Yoruba text, English glosses, language
labels, intents, or sentiment labels are semantically correct.

A partial linguistic review is documented in `reports/human_linguistic_review_report.txt`: 12 Yoruba/code-switched records had their wording and English glosses reviewed by the project owner, who is a Yoruba speaker, and one additional record had its language label confirmed. Seven English-only records were not reviewed in that pass. Intent and sentiment labels have not been independently certified.

See:

- `guidelines/annotation_guidelines.md`
- `guidelines/quality_assurance.md`
- `reports/project2_quality_report.txt`
- `reports/dataset_card.md`

## Limitations and Responsible Use

This is a small synthetic dataset for educational and portfolio purposes.
It does not represent the full diversity of Yoruba speakers, dialects,
code-switching patterns, or real-world customer messages.

The project does not claim:

- Complete independent linguistic validation of all records.
- Independent inter-annotator agreement.
- Representative sampling of Yoruba-language usage.
- Measured model performance.
- Production readiness.

Do not use the current dataset alone to draw broad conclusions about
multilingual model quality or real-world customer behavior.

## Skills Demonstrated

- Annotation schema and guideline design.
- Label Studio task preparation and annotation.
- Intent and sentiment classification.
- Multilingual data handling.
- CSV, JSON, and JSONL processing.
- Python-based validation and data cleaning.
- Quality assurance reporting.
- Dataset documentation and reproducibility.
- Responsible reporting of data limitations.

## Future Improvements

- Extend and document linguistic review to the remaining English-only records and independently verify intent and sentiment labels.
- Resolve uncertain glosses and annotations.
- Expand the dataset with a documented sampling strategy.
- Collect independent annotations if agreement analysis is required.
- Add regression tests for the processing scripts.
- Version the dataset and document subsequent changes.
- Evaluate models only after establishing an appropriate evaluation design.

## License

A license has not yet been selected for this project. Choose and document
an appropriate license before publicly redistributing the dataset.
