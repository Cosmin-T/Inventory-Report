# send_email.py

import smtplib
from datetime import datetime
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logic.util import *
import logging
from logic.logs import *
import os

conf_log()

def send(file_output, subject, file_name):
    today = datetime.now().date()
    # today = today - timedelta(days=0)

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f'{subject} - {today}'

    body = f'Please check the daily LiveVox date check for {today} at: \n{URL}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(file_output, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='txt')
            attachment.add_header('content-Disposition', 'attachment', filename=file_name)
            msg.attach(attachment)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            logging.info("Email sent successfully!")

    except Exception as e:
        logging.error(f'Exception: {e}')