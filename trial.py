#!/usr/bin/env python

import sys, shutil, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# functionn to send the mail with credentials
def send_email(recipient=None, html_m=None):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "xxxxxxxxxxxxx"
    sender_password = "xxxxxxxx"

    with smtplib.SMTP(smtp_server) as server:
        server.connect(host=smtp_server, port=port)
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Files Transfer Report"

        # message.attach(MIMEText(html_m, "html"))
        server.send_message(message)
        print("message sent")


if __name__ == "__main__":
    send_email(recipient="xxxxxxxx")