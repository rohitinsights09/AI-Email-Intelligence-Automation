import json
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Email Intelligence",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

try:
    with open("data/processed_emails.json", "r") as file:
        emails = json.load(file)

except FileNotFoundError:
    st.error("processed_emails.json not found. Run main.py first.")
    st.stop()

except json.JSONDecodeError:
    st.error("processed_emails.json contains invalid JSON.")
    st.stop()


if not emails:
    st.warning("No processed emails available.")
    st.stop()


df = pd.DataFrame(emails)


# ============================================================
# TITLE
# ============================================================

st.title("🤖 AI Email Intelligence")
st.caption(
    "AI-powered email classification, triage, approval and automation analytics"
)

st.divider()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_emails = len(df)

high_priority = len(
    df[df["priority"].astype(str).str.lower() == "high"]
)

human_approval = len(
    df[df["decision"] == "Human approval required"]
)

approved = len(
    df[df["status"] == "approved"]
)

auto_reply = len(
    df[
        df["action"]
        .astype(str)
        .str.lower()
        .str.contains("auto_reply", na=False)
    ]
)

human_review = len(
    df[
        df["action"]
        .astype(str)
        .str.lower()
        .str.contains("human_approval", na=False)
    ]
)

automation_rate = (
    round((auto_reply / total_emails) * 100, 1)
    if total_emails > 0
    else 0
)


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("📌 Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Emails",
        total_emails
    )

with col2:
    st.metric(
        "High Priority",
        high_priority
    )

with col3:
    st.metric(
        "Human Review",
        human_review
    )

with col4:
    st.metric(
        "Automation Rate",
        f"{automation_rate}%"
    )


# ============================================================
# FILTERS
# ============================================================

st.subheader("🔎 Filters")

col1, col2, col3 = st.columns(3)

with col1:
    priority_options = sorted(
        df["priority"].dropna().unique().tolist()
    )

    selected_priority = st.multiselect(
        "Priority",
        priority_options,
        default=priority_options
    )

with col2:
    category_options = sorted(
        df["category"].dropna().unique().tolist()
    )

    selected_category = st.multiselect(
        "Category",
        category_options,
        default=category_options
    )

with col3:
    sentiment_options = sorted(
        df["sentiment"].dropna().unique().tolist()
    )

    selected_sentiment = st.multiselect(
        "Sentiment",
        sentiment_options,
        default=sentiment_options
    )


filtered_df = df[
    df["priority"].isin(selected_priority)
    & df["category"].isin(selected_category)
    & df["sentiment"].isin(selected_sentiment)
]


# ============================================================
# ANALYTICS
# ============================================================

st.subheader("📊 Email Analytics")

col1, col2 = st.columns(2)

with col1:

    st.write("**Priority Distribution**")

    priority_counts = filtered_df["priority"].value_counts()

    st.bar_chart(priority_counts)


with col2:

    st.write("**Category Distribution**")

    category_counts = filtered_df["category"].value_counts()

    st.bar_chart(category_counts)


col3, col4 = st.columns(2)

with col3:

    st.write("**Sentiment Distribution**")

    sentiment_counts = filtered_df["sentiment"].value_counts()

    st.bar_chart(sentiment_counts)


with col4:

    st.write("**Automation vs Human Review**")

    automation_data = pd.Series(
        {
            "Auto Reply": auto_reply,
            "Human Review": human_review
        }
    )

    st.bar_chart(automation_data)


# ============================================================
# AUTOMATION SUMMARY
# ============================================================

st.subheader("🤖 Automation Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Auto-Reply Candidates",
        auto_reply
    )

with col2:
    st.metric(
        "Human Review",
        human_review
    )

with col3:
    st.metric(
        "Approved Emails",
        approved
    )


# ============================================================
# EMAIL TABLE
# ============================================================

st.subheader("📧 Processed Emails")

display_columns = [
    "email_id",
    "subject",
    "category",
    "priority",
    "sentiment",
    "decision",
    "status"
]

available_columns = [
    column
    for column in display_columns
    if column in filtered_df.columns
]

st.dataframe(
    filtered_df[available_columns],
    width="stretch",
    hide_index=True
)


# ============================================================
# SUMMARY
# ============================================================

st.divider()

st.caption(
    "AI Email Intelligence • Built with Python, Ollama, Pandas and Streamlit"
)