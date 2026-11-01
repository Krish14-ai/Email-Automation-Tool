# 📧 Email Automation Tool

A Python-based bulk email automation and recipient management system powered by the **Google Gmail API (v1)**, **FastAPI**, and **Pydantic**. This tool enables automated email broadcasting to recipient lists from CSV files with secure OAuth 2.0 authentication and automated token caching.

---

## 🚀 Features

- **Google Gmail API Integration**: Send emails directly through your authenticated Gmail account using Google's official REST API (`users().messages().send`).
- **OAuth 2.0 with Token Persistence**: Seamless authentication using `InstalledAppFlow` with automatic token refresh and local caching (`token_gmail_v1.pickle`).
- **Batch Email Dispatch**: Read and process recipient email lists dynamically from CSV datasets using `pandas`.
- **MIME Email Construction**: Standard MIME multipart email crafting supporting custom subjects, plain text, and HTML formatting.
- **RESTful API via FastAPI**: Built-in HTTP endpoints to query recipient records and integrate with other services.
- **Robust Data Validation**: Strict recipient schema validation powered by `Pydantic` enforcing ID formats, name length, and email format integrity.

---

## 📁 Project Structure

```text
Email-Automation-Tool/
├── client_secret.json          # Google OAuth 2.0 client credentials (downloaded from GCP)
├── token_gmail_v1.pickle       # Auto-generated cached OAuth token (git-ignored)
├── requirements.txt            # Project dependencies
├── mails/
│   └── data/
│       └── recipients.csv      # CSV file containing recipient data
├── schema/
│   ├── api.py                  # FastAPI web server and routing
│   ├── data_methods.py         # Data retrieval and helper methods
│   └── data_validate.py        # Pydantic validation models
└── src/
    ├── gmail_auth.py           # Google API authentication & service factory
    └── main.py                 # Core email dispatch automation script
```

---

## 🛠️ Prerequisites

- **Python 3.9+** installed on your system.
- A **Google Cloud Platform (GCP)** project with the **Gmail API** enabled.
- OAuth 2.0 Client ID credentials (`Desktop Application`) from GCP.

---

