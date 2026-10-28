# Yoruba-English Intent and Sentiment Annotation Guidelines

## 1. Project Purpose

This project demonstrates a structured workflow for annotating intent and sentiment in English, Yoruba, and code-switched text.

The starter dataset contains synthetic examples created for portfolio practice. They are not authentic customer conversations. Initial labels and English glosses are provisional and must be reviewed.

## 2. Annotation Fields

Annotators should review the following fields:

- `text`: Original message. Preserve it exactly.
- `language`: Main language category.
- `intent`: The user's primary communicative goal.
- `sentiment`: The emotional tone expressed in the message.
- `english_gloss`: An English translation or explanation, where applicable.

## 3. Language Labels

Use one of these labels:

- `English`: The message is primarily in English.
- `Yoruba`: The message is primarily in Yoruba.
- `code_switched`: The message meaningfully combines Yoruba and another language, such as English or Nigerian Pidgin.

Do not classify a message as code-switched merely because it contains a widely used borrowed word. Consider the message as a whole.

If language identification is uncertain, flag the example for review.

## 4. Intent Labels

Choose the label that best describes the user's main goal.

- `order_status`: Asking about an order's status or tracking.
- `payment_issue`: Reporting a payment failure, deduction, or payment-related problem.
- `refund_request`: Requesting a refund or return of money.
- `order_cancellation`: Asking to cancel an order.
- `account_access`: Reporting login or account-access problems.
- `technical_support`: Asking for help with an app, device, or technical problem.
- `product_inquiry`: Asking about a product's features, specifications, or warranty.
- `product_feedback`: Expressing an opinion about a product.
- `delivery_issue`: Reporting a delivery delay, failure, or delivery problem.
- `price_inquiry`: Asking about price, fees, or costs.
- `appreciation`: Primarily thanking or appreciating a person or service.
- `complaint`: Expressing dissatisfaction or reporting poor treatment when no more specific intent applies.
- `service_feedback`: Giving feedback about a service or an experience.
- `request_help`: Requesting assistance when a more specific intent does not apply.
- `general_inquiry`: Asking a general question about an organization or service.
- `other`: The message does not fit any available intent label.

### Intent Decision Rules

1. Label the main purpose of the message, not its emotional tone.
2. Prefer a specific label over a broad label when the evidence supports it.
3. A negative message about a payment should normally use `payment_issue` if that is its primary purpose.
4. A direct request for money back should normally use `refund_request`.
5. A complaint about an experience may use `service_feedback` when feedback is the main purpose.
6. Use `other` only when no defined label reasonably fits.
7. If two intents seem equally plausible, document the ambiguity for review.

## 5. Sentiment Labels

Choose one label:

- `positive`: The message expresses satisfaction, happiness, gratitude, or approval.
- `neutral`: The message is primarily factual or requests information without a clear positive or negative emotional tone.
- `negative`: The message expresses dissatisfaction, frustration, disappointment, or another negative emotional tone.
- `mixed`: The message clearly expresses both positive and negative sentiment.

### Sentiment Decision Rules

1. A question is not automatically negative.
2. A polite request can still express negative sentiment if dissatisfaction is clear.
3. Do not infer emotion that is not supported by the message.
4. Use `mixed` when both positive and negative sentiment are meaningfully expressed.
5. If sentiment is ambiguous, flag it for review rather than guessing.

## 6. Yoruba Text and English Glosses

1. Preserve the original Yoruba text, including tone marks and special characters.
2. Do not silently correct spelling or rewrite the source message.
3. The English gloss should preserve the meaning of the original text.
4. Do not invent context that is not present in the source.
5. Yoruba phrases may be context-dependent. If a phrase has multiple plausible interpretations, document the uncertainty.
6. Machine-generated translations must not be treated as verified ground truth.
7. Where possible, ask a competent Yoruba speaker to review the Yoruba examples and their glosses.

## 7. Code-Switching

Code-switched messages combine meaningful material from more than one language.

Examples may contain Yoruba and English, or Yoruba and Nigerian Pidgin.

Do not assume that every word has a direct one-to-one translation. Preserve the original message and provide an English gloss that captures its intended meaning.

## 8. Quality Assurance

Before approving an annotation, check:

- The record has a unique ID.
- The original text is present.
- The language label is allowed.
- The intent label is allowed.
- The sentiment label is allowed.
- The English gloss is present.
- The labels match the message meaning.
- Ambiguous expressions are documented for review.
- The original text has not been altered.

Automated validation checks structural consistency and allowed labels. It cannot independently prove that a translation or interpretation is linguistically correct.

## 9. Disagreement and Review

When an annotation is uncertain:

1. Record the disputed field.
2. Explain the competing interpretations.
3. Request review by a competent Yoruba speaker or another qualified reviewer where appropriate.
4. Update the label only when the evidence supports the decision.
5. Preserve a record of important adjudication decisions.

Do not claim inter-annotator agreement unless independent annotations have actually been collected and analyzed.

## 10. Dataset Limitations

The initial dataset is small and synthetic. It is intended to demonstrate annotation workflow and data quality practices, not to represent all Yoruba speakers, dialects, Nigerian Pidgin usage, or real-world customer messages.

The dataset must be expanded and reviewed before it is used to make claims about model performance or broad language coverage.
