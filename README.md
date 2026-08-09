# 🤖 AI Email Intelligence & Automation

An AI-powered email triage and automation system built using Python, Ollama and Streamlit.

The system analyzes incoming emails, classifies them, determines priority and sentiment, generates summaries, and decides whether an email can be handled automatically or requires human approval.

---

## 🚀 Features

- 📧 Email classification
- 🏷️ Category detection
- 🔴 Priority detection
- 😊 Sentiment analysis
- 📝 AI-generated email summaries
- 🤖 Automated decision making
- 👤 Human approval workflow
- 📊 Interactive Streamlit dashboard
- 🔎 Dashboard filters
- 📈 Email analytics
- 📋 Processed email logging
- 🧠 Local LLM using Ollama
- 🔐 Environment variable support for sensitive configuration

---

## 🏗️ Architecture

```text
Incoming Email
      ↓
Python Email Processing
      ↓
Ollama Local LLM
      ↓
AI Analysis
      ↓
┌───────────────────────────────┐
│ Category                      │
│ Priority                      │
│ Sentiment                     │
│ Summary                       │
│ Decision                      │
└───────────────────────────────┘
      ↓
Risk / Decision Logic
      ↓
 ┌───────────────┬────────────────┐
 │               │                │
 ▼               ▼                │
Auto Reply    Human Approval      │
 │               │                │
 └───────────────┴────────────────┘
              ↓
       Processed JSON
              ↓
      Streamlit Dashboard

      ---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Ollama | Local LLM / AI processing |
| Pandas | Data processing and analysis |
| Streamlit | Interactive dashboard |
| JSON | Email data storage |

---

## 📂 Project Structure

```text
AI Email Triage/
│
├── data/
│   ├── sample_emails.json
│   └── processed_emails.json
│
├── logs/
│
├── src/
│   ├── main.py
│   ├── dashboard.py
│   └── dashboard_backup.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

⚙️ How It Works
1. Email Input

The system receives email information such as sender, subject and email body.

2. AI Analysis

Ollama processes the email and extracts structured information including:

Category
Priority
Sentiment
Summary
Decision
3. Decision Logic

The system determines whether an email can be handled automatically or requires human approval.

4. Data Storage

Processed email information is stored in JSON format.

5. Dashboard

Streamlit displays the processed information through an interactive analytics dashboard.

📊 Dashboard

The dashboard provides:

Total email count
High-priority email count
Human review count
Automation rate
Priority distribution
Category distribution
Sentiment distribution
Automation analytics
Interactive filters
Processed email table
💻 Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project
cd AI-Email-Triage
3. Install dependencies
pip install -r requirements.txt
4. Install and run Ollama

Make sure Ollama is installed and the required local model is available.

5. Run the AI email processor
python src/main.py
6. Run the dashboard
python -m streamlit run src/dashboard.py

The dashboard will open at:

http://localhost:8501
🔐 Environment Variables

Sensitive configuration should be stored in a .env file.

Example:

API_KEY=your_api_key_here

Never upload .env or API keys to GitHub.

🎯 Skills Demonstrated

This project demonstrates practical experience with:

Python
Generative AI
Local LLMs
Ollama
JSON
AI classification
Information extraction
Decision logic
Human-in-the-loop automation
Pandas
Streamlit
Data visualization
Error handling
Logging
Git/GitHub
🔮 Future Improvements
Gmail API integration
Outlook integration
Automatic reply drafting
Human approval interface
Database integration
Email attachment analysis
Scheduled email processing
Advanced analytics
Production deployment

## 👨‍💻 Author

**Rohit Ravindra Shinde**

AI & Data Analytics Portfolio Project

⭐ Project Highlights

AI Email Intelligence & Automation

Python + Local LLM + AI Automation + Data Analysis + Streamlit

An end-to-end project designed to demonstrate how AI can be used to classify, analyze and automate email workflows.

<img width="882" height="685" alt="image" src="https://github.com/user-attachments/assets/735faeb7-8064-4b36-905b-2b9db993cf9e" />
<img width="877" height="677" alt="image" src="https://github.com/user-attachments/assets/1ff91abf-57c1-42f9-a2e6-817f0c94bd76" />

