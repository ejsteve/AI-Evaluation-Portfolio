from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_DIR / "data" / "evaluation_predictions.csv"
RESULTS_DIR = PROJECT_DIR / "results" / "metrics"


def main() -> None:
    print("=" * 60)
    print("PROJECT 01 - AI PREDICTION EVALUATION")
    print("=" * 60)

    if not DATA_FILE.exists():
        print("\nPrediction file not found yet:")
        print(DATA_FILE)

        print(
            "\nThis is expected at this stage.\n"
            "We will create this file after Label Studio\n"
            "human annotation and AgentRouter inference."
        )
        return

    df = pd.read_csv(DATA_FILE)

    required_columns = {
        "id",
        "text",
        "human_label",
        "ai_prediction",
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    y_true = df["human_label"]
    y_pred = df["ai_prediction"]

    accuracy = accuracy_score(y_true, y_pred)

    report = classification_report(
        y_true,
        y_pred,
        zero_division=0,
    )

    matrix = confusion_matrix(y_true, y_pred)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    metrics_file = RESULTS_DIR / "classification_report.txt"

    with metrics_file.open("w", encoding="utf-8") as f:
        f.write("PROJECT 01 - SENTIMENT EVALUATION\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Accuracy: {accuracy:.4f}\n\n")
        f.write("Classification Report\n")
        f.write("-" * 60 + "\n")
        f.write(report)
        f.write("\nConfusion Matrix\n")
        f.write("-" * 60 + "\n")
        f.write(str(matrix))

    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)

    print("\nConfusion Matrix:")
    print(matrix)

    print(f"\nSaved results to: {metrics_file}")


if __name__ == "__main__":
    main()
