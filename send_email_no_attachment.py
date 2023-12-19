import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "type here your_iost_account@gmail.com"
email_password ="type here your_iost_account@ gmail KEY here"
email_send = "type here the email_address you want to send an email to"

subject = "type here the subject line of your email"

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_send
msg["Subject"] = subject

body = "Type here the message you wish to send"
msg.attach(MIMEText(body,"plain"))

text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()
#does nothing