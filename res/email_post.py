import smtplib


def send_mail(mail_send: str):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('Почта', 'Пароль')

    SUBJECT = "Test result"
    TO = "Откого"
    FROM = "Кому"
    text = mail_send
    BODY = "\r\n".join(("From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "", text))

    smtpObj.sendmail(FROM, [TO], BODY)
    smtpObj.quit()
