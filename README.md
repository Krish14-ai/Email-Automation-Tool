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

## ⚙️ Google Cloud & Gmail API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (e.g., `Email-Automation`).
3. Navigate to **APIs & Services** > **Library** and search for **Gmail API**. Click **Enable**.
4. Go to **APIs & Services** > **OAuth consent screen**:
   - Choose **External** (or **Internal** if using Google Workspace).
   - Add your test email under **Test users**.
   - Add the scope: `https://www.googleapis.com/auth/gmail.send`.
5. Navigate to **APIs & Services** > **Credentials**:
   - Click **Create Credentials** > **OAuth client ID**.
   - Select **Desktop App** as the Application type.
   - Download the JSON file, rename it to `client_secret.json`, and place it in the project root directory.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Krish14-ai/Email-Automation-Tool.git
   cd Email-Automation-Tool
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv myenv
     myenv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > *Note: Ensure all required packages are installed:*
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas fastapi uvicorn "pydantic[email]"
   ```

---

## 📋 Recipient Data Configuration

Define your recipients in [mails/data/recipients.csv](file:///mails/data/recipients.csv):

```csv
user_id,name,mail
001,John Doe,johndoe@example.com
002,Jane Smith,janesmith@example.com
```

### Validation Schema (`schema/data_validate.py`)
The `Mails` Pydantic model enforces the following constraints:
- `user_id`: Must be exactly 3 numeric digits (e.g., `001`, `042`).
- `name`: Must be between 2 and 100 characters.
- `mail`: Must be a valid email string (`EmailStr`) with custom business validation.

---

## 💻 Usage

### 1. Send Bulk Emails

Run the main automation script:

```bash
python src/main.py
```

- On your first run, a browser tab will open requesting permission to access your Gmail account.
- Once authorized, a token named `token_gmail_v1.pickle` will be generated locally for future executions.
- The script iterates through `recipients.csv` and dispatches the configured email to each contact.

### 2. Run the FastAPI Service

To query recipient information and run the web service:

```bash
uvicorn schema.api:app --reload
```

- **Interactive API Documentation (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Documentation (Redoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Available Endpoints:
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check endpoint returning a welcome message |
| `GET` | `/mails` | Returns the list of all recipient emails from the CSV database |

---

## 🔒 Security Best Practices

- **Never commit credentials**: Ensure that `client_secret.json` and `token_*.pickle` are included in your `.gitignore` to avoid publishing sensitive tokens.
- **Principle of Least Privilege**: The application uses the restricted `https://www.googleapis.com/auth/gmail.send` scope, granting write-only access without read access to your inbox.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).