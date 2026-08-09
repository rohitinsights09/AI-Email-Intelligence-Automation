import json
import logging
from ollama import chat


# -----------------------------
# Logging setup
# -----------------------------

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# -----------------------------
# Load email data
# -----------------------------

try:
    with open("data/sample_emails.json", "r") as file:
        emails = json.load(file)

except FileNotFoundError:
    print("❌ Error: sample_emails.json was not found.")
    logging.error("sample_emails.json was not found.")
    exit()

except json.JSONDecodeError:
    print("❌ Error: sample_emails.json contains invalid JSON.")
    logging.error("sample_emails.json contains invalid JSON.")
    exit()


# -----------------------------
# Store processed results
# -----------------------------

processed_emails = []


# -----------------------------
# Process each email
# -----------------------------

for email in emails:

    email_id = email.get("id", "Unknown")

    print("\nProcessing Email:", email_id)

    subject = email.get("subject", "")
    body = email.get("body", "")

    if not subject or not body:

        print("❌ Email is missing subject or body.")

        logging.warning(
            f"Email {email_id} | Missing subject or body"
        )

        continue


    # -----------------------------
    # AI analysis prompt
    # -----------------------------

    prompt = f"""
You are an AI email triage assistant.

Analyze the customer email below.

Subject: {subject}
Body: {body}

Return ONLY valid JSON.
Do not add markdown.
Do not add explanations.

Use exactly these fields:

The category MUST be exactly ONE of these values:
billing, technical, account, general, other.

Do not return multiple categories.
Do not return the category options as the value.

{{
    "category": "billing",
    "priority": "high, medium, or low",
    "sentiment": "positive, neutral, or negative",
    "summary": "short summary of the issue",
    "action": "auto_reply or human_approval"
}}
"""


    # -----------------------------
    # Call AI
    # -----------------------------

    try:

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    except Exception as e:

        print("❌ AI connection error:", e)

        logging.error(
            f"Email {email_id} | AI connection error | {e}"
        )

        continue


    # -----------------------------
    # Parse AI JSON
    # -----------------------------

    ai_result = response["message"]["content"]

    try:

        result = json.loads(ai_result)

    except json.JSONDecodeError:

        print("❌ AI returned invalid JSON.")

        logging.error(
            f"Email {email_id} | Invalid AI JSON"
        )

        continue


    category = result.get("category", "unknown")
    priority = result.get("priority", "unknown")
    sentiment = result.get("sentiment", "unknown")
    summary = result.get("summary", "unknown")
    action = result.get("action", "unknown")


    print("Category:", category)
    print("Priority:", priority)
    print("Sentiment:", sentiment)
    print("Summary:", summary)
    print("Action:", action)


    # -----------------------------
    # Decision logic
    # -----------------------------

    if priority == "high":

        decision = "Human approval required"

    elif action == "human_approval":

        decision = "Human approval required"

    else:

        decision = "Safe for auto-reply"


    print("Decision:", decision)


    # -----------------------------
    # Human approval / Auto reply
    # -----------------------------

    if decision == "Human approval required":

        print("\n⚠️ This email requires human approval.")

        approval = input(
            "Do you want to approve a reply? (yes/no): "
        ).strip().lower()

        if approval == "yes":

            status = "approved"

            print("✅ Reply approved.")

        elif approval == "no":

            status = "rejected"

            print("❌ Reply rejected.")

        else:

            status = "rejected"

            print("⚠️ Invalid input. Reply rejected.")


    else:

        reply_prompt = f"""
You are a professional customer support assistant.

Write a short and polite reply to this customer email.

Subject: {subject}
Body: {body}

Customer issue:
{summary}

Rules:
- Be professional and helpful.
- Do not invent information.
- Do not promise refunds, credits, or actions that are not confirmed.
- Keep the reply concise.
"""


        try:

            reply_response = chat(
                model="qwen2.5:3b",
                messages=[
                    {
                        "role": "user",
                        "content": reply_prompt
                    }
                ]
            )

            draft_reply = reply_response["message"]["content"]

            print("\nDraft Reply:")
            print(draft_reply)

        except Exception as e:

            print("❌ Error generating reply:", e)

            logging.error(
                f"Email {email_id} | Reply generation error | {e}"
            )

            continue


        approval = input(
            "\nApprove this reply? (yes/no): "
        ).strip().lower()

        if approval == "yes":

            status = "approved"

            print("✅ Reply approved.")

        elif approval == "no":

            status = "rejected"

            print("❌ Reply rejected.")

        else:

            status = "rejected"

            print("⚠️ Invalid input. Reply rejected.")


    # -----------------------------
    # Save result in memory
    # -----------------------------

    processed_email = {
        "email_id": email_id,
        "subject": subject,
        "category": category,
        "priority": priority,
        "sentiment": sentiment,
        "summary": summary,
        "action": action,
        "decision": decision,
        "status": status
    }

    processed_emails.append(processed_email)


    # -----------------------------
    # Logging
    # -----------------------------

    logging.info(
        f"Email {email_id} | "
        f"Category: {category} | "
        f"Priority: {priority} | "
        f"Sentiment: {sentiment} | "
        f"Decision: {decision} | "
        f"Status: {status}"
    )

    print("📝 Activity logged.")
    print("-" * 60)


# -----------------------------
# Save all processed results
# -----------------------------

try:

    with open("data/processed_emails.json", "w") as file:

        json.dump(
            processed_emails,
            file,
            indent=4
        )

    print("\n✅ Processed results saved successfully.")

except Exception as e:

    print("❌ Error saving processed results:", e)

    logging.error(
        f"Error saving processed results | {e}"
    )