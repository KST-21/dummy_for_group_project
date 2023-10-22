from email.message import EmailMessage
import smtplib
import ssl
import random

server = "neymar21112002born@gmail.com"
user = "www.kst21112002@gmail.com"
password = "xret htuj tlqy dqgy"
subject = "Verify Email"
verification_code = random.randint(100000, 999999)
body = f"""
Verification code:
{verification_code}
Someone tried to use this ({user}) email to sign up Guide4u. If this was you, please use the code above to confirm your identity.
"""

email_message = EmailMessage()
email_message["from"] = server
email_message["to"] = user
email_message["subject"] = subject
email_message.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    try:
        smtp.login(server, password)
        smtp.sendmail(server, user, email_message.as_string())
    except:
        print("Failed!")