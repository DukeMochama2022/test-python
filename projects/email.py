from email.message import EmailMessage
import ssl
import smtplib

email_sender='dukemochama21@gmail.com'
email_password="mcbs mjad rgjj zoir"

email_receiver="dukemochama21@gmail.com"
subject="Testing skillset in Python"
body="Hello i love you much"

em=EmailMessage()

em['from']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")