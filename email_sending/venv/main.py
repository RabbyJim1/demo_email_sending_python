import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "rabby.jim999@gmail.com"
email["to"] = "jim15-5551@diu.edu.bd"
email["subject"] = "Test Email"

content = '''This is a test/demo email.
please don't reply to this email'''
email.set_content(content)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login("rabby.jim999@gmail.com", "40408080")
    smtp.send_message(email)
