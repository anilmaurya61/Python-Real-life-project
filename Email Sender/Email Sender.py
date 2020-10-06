import smtplib
to = import("Enter The Email Of Recipent :\n")

content = input("Enter The Content Of Email:\n")

def send_mail(to, content):
    server = smtlib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sendermail@gmail.com",'1234')
    server.sendmail("sendmail@gmail.com", to, content)
    server.close()

sendEmail(to, content)
