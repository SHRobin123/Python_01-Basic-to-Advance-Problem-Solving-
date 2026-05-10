#Email Sender Example

import smtplib
from email.mime.text import MIMEText

# sender info
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"

# email content
subject = "Test Email from Python"
body = "Hello! This is a test email sent using Python."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    # connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # login
    server.login(sender_email, password)

    # send email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

    print("Email sent successfully")

except Exception as e:
    print("Error:", e)

'''
output:-

Email sent successfully
'''