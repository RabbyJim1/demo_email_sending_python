import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

email = EmailMessage()
email["from"] = "rabby.jim999@gmail.com"
email["to"] = "jim15-5551@diu.edu.bd"
# email["subject"] = "Test Email"

html = Template(Path("email_body.html").read_text())


email.set_content(html.substitute({"name": "jim"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login("rabby.jim999@gmail.com", "40408080")
    smtp.send_message(email)
