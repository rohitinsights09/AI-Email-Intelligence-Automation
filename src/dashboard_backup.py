import json
import pandas as pd
import streamlit as st


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Email Intelligence",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Load processed email data
# -----------------------------

try:

    with open("data/processed_emails.json", "r") as file:
        emails = json.load(file)

except FileNotFoundError:

    st.error("processed_emails.json not found. Run main.py first.")
    st.stop()

except json.JSONDecodeError:

    st.error("processed_emails.json contains invalid JSON.")
    st.stop()


# -----------------------------
# Convert JSON to DataFrame
# -----------------------------

df = pd.DataFrame(emails)


# -----------------------------
# Dashboard title
# -----------------------------

st.title("🤖 AI Email Intelligence Dashboard")

st.write(
    "AI-powered email classification, decision tracking and automation overview."
)


# -----------------------------
# KPI Cards
# -----------------------------

total_emails = len(df)

high_priority = len(
    df[df["priority"].str.lower() == "high"]
)

human_approval = len(
    df[df["decision"] == "Human approval required"]
)

approved = len(
    df[df["status"] == "approved"]
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Emails", total_emails)

with col2:
    st.metric("High Priority", high_priority)

with col3:
    st.metric("Human Approval", human_approval)

with col4:
    st.metric("Approved", approved)

# -----------------------------
# Automation Analytics
# -----------------------------

st.subheader("🤖 Automation Analytics")

auto_reply = len(
    df[df["action"].str.lower().str.contains("auto_reply", na=False)]
)

human_review = len(
    df[df["action"].str.lower().str.contains("human_approval", na=False)]
)

if total_emails > 0:
    automation_rate = round((auto_reply / total_emails) * 100, 1)
    human_review_rate = round((human_review / total_emails) * 100, 1)
else:
    automation_rate = 0
    human_review_rate = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🤖 Auto-Reply Candidates",
        auto_reply
    )

with col2:
    st.metric(
        "👤 Human Review",
        human_review
    )

with col3:
    st.metric(
        "⚡ Automation Rate",
        f"{automation_rate}%"
    )


# -----------------------------
# Email data table
# -----------------------------

st.subheader("📧 Processed Emails")

st.dataframe(
    df,
    width="stretch"
)
# -----------------------------
# Filters
# -----------------------------

st.subheader("🔎 Dashboard Filters")

col1, col2, col3 = st.columns(3)

with col1:
    priority_filter = st.multiselect(
        "Priority",
        options=df["priority"].dropna().unique(),
        default=df["priority"].dropna().unique()
    )

with col2:
    category_filter = st.multiselect(
        "Category",
        options=df["category"].dropna().unique(),
        default=df["category"].dropna().unique()
    )

with col3:
    sentiment_filter = st.multiselect(
        "Sentiment",
        options=df["sentiment"].dropna().unique(),
        default=df["sentiment"].dropna().unique()
    )

filtered_df = df[
    df["priority"].isin(priority_filter)
    & df["category"].isin(category_filter)
    & df["sentiment"].isin(sentiment_filter)
]

# -----------------------------
# Charts
# -----------------------------

st.subheader("📊 Email Analytics")

col1, col2 = st.columns(2)

with col1:
    st.write("### Priority Distribution")

    priority_counts = filtered_df["priority"].value_counts()

    st.bar_chart(priority_counts)

with col2:
    st.write("### Category Distribution")

    category_counts = filtered_df["category"].value_counts()

    st.bar_chart(category_counts)

col3, col4 = st.columns(2)

with col3:
    st.write("### Sentiment Distribution")

    sentiment_counts = filtered_df["sentiment"].value_counts()

    st.bar_chart(sentiment_counts)

with col4:
    st.write("### Decision Distribution")

    decision_counts = filtered_df["decision"].value_counts()

    st.bar_chart(decision_counts)

# -----------------------------
# Filtered Email Results
# -----------------------------

st.subheader("📋 Filtered Results")

st.dataframe(
    filtered_df,
    width="stretch"
)