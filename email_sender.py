import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sender'
email['to'] = 'exampleemail@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content('I am a python master')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('senders_email_adress@gmail.com', 'account_password')
    smtp.send_message(email)
    print('Message Sent')
