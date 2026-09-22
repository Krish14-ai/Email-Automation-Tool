from gmail_auth import Create_Service 
import base64
from email.mime.multipart import MIMEMultipart

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION= 'v1'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)