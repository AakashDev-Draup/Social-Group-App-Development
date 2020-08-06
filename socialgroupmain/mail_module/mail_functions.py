
import smtplib

# list of email_id to send the mail
# recipients = ["xxxxx@gmail.com", "yyyyy@gmail.com"]


def send_mail(recipients,content):
    for dest in recipients:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("demosocialapptest@gmail.com", "Demo@test1234")
        # message = "Message_you_need_to_send"
        s.sendmail("demosocialapptest@gmail.com", dest, content)
        s.quit()
