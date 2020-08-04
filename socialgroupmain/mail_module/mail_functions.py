
import smtplib

# list of email_id to send the mail
# recipients = ["xxxxx@gmail.com", "yyyyy@gmail.com"]


def send_mail(recipients,content):
    for dest in recipients:
        s = smtplib.SMTP('smtp.gmail.com', 27017)
        s.starttls()
        s.login("emailid", "password")
        message = "Message_you_need_to_send"
        s.sendmail("senders email", dest, message)
        s.quit()
