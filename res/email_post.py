import smtplib


def send_mail(mail_send: str):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('stobebydeveloper@gmail.com', 'Dsd3234bfqq44234m')

    SUBJECT = "Test result"
    TO = "fastscrul@gmail.com"
    # TO = "bashlykova_a_a_mirea@mail.ru"
    FROM = "stobebydeveloper@gmail.com"

    BODY = "\r\n".join(("From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "", mail_send))

    smtpObj.sendmail(FROM, [TO], BODY)
    smtpObj.quit()
