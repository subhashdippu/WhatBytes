import smtplib
from django.core.mail import EmailMessage
import os


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.send()


email_sender = os.environ.get('EMAIL_FROM')
# email_password = password
email_receiver = 'subhashprasad2001@gmail.com'

subject = 'Testing'
body = 'This is Subhash Prasad Testing message'

text = f"Subject:{subject}\n\n{body}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email_sender, "upau boxo fzyw llph")
server.sendmail(email_sender, email_receiver, text)
print('message send')
