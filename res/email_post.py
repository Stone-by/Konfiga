import smtplib


def send_mail(mail_send: str):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('stobebydeveloper@gmail.com', 'Dsd3234bfqq44234m')

    SUBJECT = "Test result"
    TO = "stobebydeveloper@gmail.com"
    FROM = "stobebydeveloper@gmail.com"
    text = mail_send
    BODY = "\r\n".join(("From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "", text))

    smtpObj.sendmail(FROM, [TO], BODY)
    smtpObj.quit()
