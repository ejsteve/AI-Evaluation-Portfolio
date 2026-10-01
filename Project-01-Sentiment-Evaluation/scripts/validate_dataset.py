from pathlib import Path
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "sentiment_seed.csv"

REQUIRED_COLUMNS = {"id", "text"}


def main() -> None:
    print("=" * 60)
    print("PROJECT 01 - SENTIMENT DATASET VALIDATION")
    print("=" * 60)

    print(f"\nDataset: {DATA_FILE}")

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    missing_ids = int(df["id"].isna().sum())
    missing_texts = int(df["text"].isna().sum())
    duplicate_ids = int(df["id"].duplicated().sum())

    empty_texts = int(
        df["text"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print("\nDATA QUALITY CHECKS")
    print("-" * 60)
    print(f"Missing IDs:     {missing_ids}")
    print(f"Missing texts:   {missing_texts}")
    print(f"Duplicate IDs:   {duplicate_ids}")
    print(f"Empty texts:     {empty_texts}")

    passed = (
        not missing_columns
        and missing_ids == 0
        and missing_texts == 0
        and duplicate_ids == 0
        and empty_texts == 0
    )

    print("\nRESULT")
    print("-" * 60)

    if passed:
        print("PASS - Dataset passed all validation checks.")
    else:
        print("FAIL - Dataset requires correction before evaluation.")

    print("=" * 60)


if __name__ == "__main__":
    main()
