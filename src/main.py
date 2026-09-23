from gmail_auth import Create_Service 
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION= 'v1'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailmsg = 'hlo bruh'
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'kkhandelwal292@gmail.com'
mimeMessage['subject'] = "greetings"
mimeMessage.attach(MIMETEXT(emailmsg,'plan'))

raw_string = base64.urlsafe_b64decode(mimeMessage.as_bytes().decode())

message = service.users().messages().send(userID = 'me',body = {'raw' : raw_string}).execute()

print(message)