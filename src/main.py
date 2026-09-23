from gmail_auth import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailmsg = 'hlo bruh'

df = pd.read_csv(
    r"C:\Users\Krish\Downloads\Email-Automation-Tool\mails\data\recipients.csv"
)

print(df)

for mail in df['mail']:

    mimeMessage = MIMEMultipart()

    mimeMessage['to'] = mail
    mimeMessage['subject'] = "greetings"

    mimeMessage.attach(
        MIMEText(emailmsg, 'plain')
    )

    raw_string = base64.urlsafe_b64encode(
        mimeMessage.as_bytes()
    ).decode()

    message = service.users().messages().send(
        userId='me',
        body={'raw': raw_string}
    ).execute()

    print(f"Email sent to {mail}")