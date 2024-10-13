import os
import smtplib, ssl
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()
# App password from .env
app_password = os.environ.get("GMAIL_APP_PASSWORD")

# https://realpython.com/python-send-email/

# Send email from python, untested.

# This doesn't work, gmail complains about the email not having SPF or DKIM authentication.
# I don't know what those are so I'll deal with it later.
# I had this working before.

port = 587

sender_email = "kelson@kelsoncraft.net"
smtp_server = "smtp.gmail.com"
recv_email = "chippy889@gmail.com"

context = ssl.create_default_context()

# def send_email():
#     # Moved to getting from .env file
#     #password = input("Enter your password: ")
#
#     message = """\
#     Subject: Hello kelson8
#
#
#     Message sent from python."""
#
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         # Login
#         server.login(sender_email, app_password)
#
#         # Send the email
#         server.sendmail(sender_email, recv_email, message)

def send_email():
    message = """\
    Subject: Hello kelson8


    Message sent from python."""
    server = smtplib.SMTP(smtp_server, port)

    try:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        # Login
        server.login(sender_email, password=app_password)
        # Send the email
        server.sendmail(sender_email, recv_email, message)


    except Exception as e:
        print(e)
    finally:
        server.quit()

if __name__ == '__main__':
    try:
        send_email()
    except KeyboardInterrupt:
        pass
