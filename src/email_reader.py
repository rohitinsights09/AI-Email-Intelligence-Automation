import json

with open("data/sample_emails.json", "r") as file:
    emails = json.load(file)

for email in emails:
    print("Email ID:", email["id"])
    print("From:", email["sender"])
    print("Subject:", email["subject"])
    print("Body:", email["body"])
    print("-" * 50)