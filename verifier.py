import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'neymar21112002born@gmail.com'
sender_password = 'xret htuj tlqy dqgy'
recipient_email = 'www.kst21112002@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create a message container
msg = MIMEMultipart()

# Email subject
msg['Subject'] = 'Formatted Email Example'

# Email body (plain text)
text = "This is a plain text email message with some formatting:\n\n"
text += "1. Bullet point 1\n"
text += "2. Bullet point 2\n"
text += "3. You can also include links: https://www.example.com"
text_part = MIMEText(text, 'plain')
msg.attach(text_part)

# Email body (HTML)
html = """
<html>
<head></head>
<body>
    <p>This is an HTML email message with formatting:</p>
    <ul>
        <li>Bullet point 1</li>
        <li>Bullet point 2</li>
    </ul>
    <p>You can also include <a href="https://www.example.com">links</a>.</p>
</body>
</html>
"""
html_part = MIMEText(html, 'html')
msg.attach(html_part)

# Create an SMTP connection and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Error sending email: {str(e)}")