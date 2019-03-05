#!/usr/bin/env python

import sys, shutil, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# functionn to send the mail with credentials
def send_email(recipient=None, html_m=None):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "xxxxxxx"
    sender_password = "xxxxxxx"

    with smtplib.SMTP(smtp_server) as server:
        server.connect(host=smtp_server, port=port)
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Files Transfer Report"

        message.attach(MIMEText(html_m, "html"))
        server.send_message(message)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        raise Exception("file_transfer.py requires a src and dest arguments") #if the source file and destination not specified


  


    src = sys.argv[1]
    dest = sys.argv[2]

    # check if the file already exist
    if os.path.exists(dest):
        # shutil.rmtree(dest)
        shutil.move(src, dest)
    

    files_count = len(os.listdir(dest))
    html_m = """
               <p>Transfered <strong>{files_count}</strong> file(s) from <strong>{src}</strong> to <strong>{dest}</strong></p>
            """.format(src=os.path.abspath(src), dest=os.path.abspath(dest), files_count=files_count)
    send_email(recipient="xxxxxxx", html_m=html_m)


