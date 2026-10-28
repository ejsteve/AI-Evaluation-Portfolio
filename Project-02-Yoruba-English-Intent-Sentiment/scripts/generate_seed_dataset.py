
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_FILE = PROJECT_DIR / "data" / "raw" / "seed_examples.csv"

# Synthetic examples for portfolio training.
# Labels are provisional and must be reviewed during annotation.
rows = [
    {
        "id": "YOR001",
        "text": "Good morning. How can I track my order?",
        "language": "English",
        "intent": "order_status",
        "sentiment": "neutral",
        "english_gloss": "Good morning. How can I track my order?",
    },
    {
        "id": "YOR002",
        "text": "Ẹ káàárọ̀, ẹ jọ̀ọ́ ẹ ràn mí lọ́wọ́.",
        "language": "Yoruba",
        "intent": "request_help",
        "sentiment": "neutral",
        "english_gloss": "Good morning, please help me.",
    },
    {
        "id": "YOR003",
        "text": "My money was deducted but I did not receive a receipt.",
        "language": "English",
        "intent": "payment_issue",
        "sentiment": "negative",
        "english_gloss": "My money was deducted but I did not receive a receipt.",
    },
    {
        "id": "YOR004",
        "text": "Owó ti jáde ní àkáǹtì mi, ṣùgbọ́n mi ò rí ìwé-ẹ̀rí ìsanwó.",
        "language": "Yoruba",
        "intent": "payment_issue",
        "sentiment": "negative",
        "english_gloss": "Money was deducted from my account, but I did not receive a payment receipt.",
    },
    {
        "id": "YOR005",
        "text": "Ẹ jọ̀ọ́, ẹ dá owó mi padà.",
        "language": "Yoruba",
        "intent": "refund_request",
        "sentiment": "negative",
        "english_gloss": "Please refund my money.",
    },
    {
        "id": "YOR006",
        "text": "Please cancel my order before it ships.",
        "language": "English",
        "intent": "order_cancellation",
        "sentiment": "neutral",
        "english_gloss": "Please cancel my order before it ships.",
    },
    {
        "id": "YOR007",
        "text": "Mo fẹ́ fagilé order mi.",
        "language": "code_switched",
        "intent": "order_cancellation",
        "sentiment": "neutral",
        "english_gloss": "I want to cancel my order.",
    },
    {
        "id": "YOR008",
        "text": "Mi ò lè wọlé sí àkáǹtì mi.",
        "language": "Yoruba",
        "intent": "account_access",
        "sentiment": "negative",
        "english_gloss": "I cannot log in to my account.",
    },
    {
        "id": "YOR009",
        "text": "This app kò ṣiṣẹ́ on my phone.",
        "language": "code_switched",
        "intent": "technical_support",
        "sentiment": "negative",
        "english_gloss": "This app does not work on my phone.",
    },
    {
        "id": "YOR010",
        "text": "Does this phone come with a warranty?",
        "language": "English",
        "intent": "product_inquiry",
        "sentiment": "neutral",
        "english_gloss": "Does this phone come with a warranty?",
    },
    {
        "id": "YOR011",
        "text": "Ẹ ṣé gan-an fún ìrànlọ́wọ́ yín.",
        "language": "Yoruba",
        "intent": "appreciation",
        "sentiment": "positive",
        "english_gloss": "Thank you very much for your help.",
    },
    {
        "id": "YOR012",
        "text": "Your support team solved my problem quickly. Thank you!",
        "language": "English",
        "intent": "appreciation",
        "sentiment": "positive",
        "english_gloss": "Your support team solved my problem quickly. Thank you!",
    },
    {
        "id": "YOR013",
        "text": "Ẹ kò tíì fi ọjà náà ránṣẹ́.",
        "language": "Yoruba",
        "intent": "delivery_issue",
        "sentiment": "negative",
        "english_gloss": "You have not sent the item yet.",
    },
    {
        "id": "YOR014",
        "text": "Abeg, ẹ check order mi.",
        "language": "code_switched",
        "intent": "order_status",
        "sentiment": "neutral",
        "english_gloss": "Please check my order.",
    },
    {
        "id": "YOR015",
        "text": "How much does delivery cost?",
        "language": "English",
        "intent": "price_inquiry",
        "sentiment": "neutral",
        "english_gloss": "How much does delivery cost?",
    },
    {
        "id": "YOR016",
        "text": "Ọjà yìí wù mí gan-an!",
        "language": "Yoruba",
        "intent": "product_feedback",
        "sentiment": "positive",
        "english_gloss": "I really like this product!",
    },
    {
        "id": "YOR017",
        "text": "I like the product, but delivery was too slow.",
        "language": "English",
        "intent": "service_feedback",
        "sentiment": "mixed",
        "english_gloss": "I like the product, but delivery was too slow.",
    },
    {
        "id": "YOR018",
        "text": "Ẹ ṣe iṣẹ́ yín dáadáa, ṣùgbọ́n delivery pẹ́ jù.",
        "language": "code_switched",
        "intent": "service_feedback",
        "sentiment": "mixed",
        "english_gloss": "You did your work well, but delivery was too late.",
    },
    {
        "id": "YOR019",
        "text": "I am unhappy with how my complaint was handled.",
        "language": "English",
        "intent": "complaint",
        "sentiment": "negative",
        "english_gloss": "I am unhappy with how my complaint was handled.",
    },
    {
        "id": "YOR020",
        "text": "Ẹ jọ̀ọ́, ẹ sọ fún mi nípa iṣẹ́ yín.",
        "language": "Yoruba",
        "intent": "general_inquiry",
        "sentiment": "neutral",
        "english_gloss": "Please tell me about your service.",
    },
]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

fieldnames = [
    "id",
    "text",
    "language",
    "intent",
    "sentiment",
    "english_gloss",
]

with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Created: {OUTPUT_FILE}")
print(f"Rows: {len(rows)}")
print("Languages:", sorted({row["language"] for row in rows}))
print("Intents:", len({row["intent"] for row in rows}))
print("Sentiment labels:", sorted({row["sentiment"] for row in rows}))
print("Note: examples and labels are synthetic and provisional.")
