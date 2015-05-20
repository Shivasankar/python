from email.mime.text import MIMEText
import email.Utils
import smtplib

emailList = [""] # this is List of Email Ids

for emailID in emailList:
    try:
        print "Sending email to", emailID
        FROM = ""           #Your Email ID
        TO = emailID
        message = "This Email is send by Python\n Python is Great !!!"
        msg = MIMEText(message)
        msg["Subject"] = "Email Notification by Python"
        msg["Message-id"] = email.Utils.make_msgid()
        msg["From"] = FROM
        msg["To"] = TO
        host = "smtp.gmail.com"
        port = "587"
        username = ""
        password = ""         #Your Password
        server = smtplib.SMTP()
        server.connect(host, port)
        print server
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.login(username,password)
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print "Email Send"
    except Exception, e:
        print e
