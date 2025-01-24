
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # Add attachment if provided
        if attachment_path:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={filename}'
                )
                msg.attach(part)

        # Connect to the email server and send
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example Usage
sender_email = "dukemochama21@gmail.com"
sender_password = "chzk cgcj dyxh dqhx"
recipient_email = "dukemochama21@gmail.com"
subject = "Hello from Python"
body = "This is a test email sent using Python!"
attachment_path = ""  # Change or leave as None if no attachment

send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)
