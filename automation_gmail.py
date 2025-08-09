from imapclient import IMAPClient
import os
from dotenv import load_dotenv
import schedule
import time
import smtplib
from email.mime.text import MIMEText


#Berichtsheft reminder for private and work mail
load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
WORK_EMAIL = os.getenv("EMAIL_ADDRESS_WORK")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# IMAP_SERVER = "imap.gmail.com" later project
# with IMAPClient(IMAP_SERVER, ssl=True) as server:
    # server.login(EMAIL, PASSWORD)

def loadBerichtsheftReminder():
    message = MIMEText("Schreibe dein Berichtsheft!")
    message["Subject"] = "Berichtsheft"
    message["From"] = EMAIL
    message["To"] = f"{EMAIL},{WORK_EMAIL}"

    SMTP_SERVER = "smtp.gmail.com"
    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(message)

#schedule.every(1).minutes.do(loadBerichtsheftReminder) #for testing purposes
schedule.every().friday.at("16:30").do(loadBerichtsheftReminder)

print("Script läuft!")

while True:
    schedule.run_pending()
    time.sleep(1)


