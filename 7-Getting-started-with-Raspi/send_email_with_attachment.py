import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''TYPE YOUR
MESSAGE
HERE'''
#The mail addresses and password
#change the next 3 lines
sender_address = 'YOUR_pcomp_CLASS_ACCOUNT@gmail.com'
sender_pass = 'YOUR_pcomp_key'
receiver_address = "EMAIL_YOU_WANT_TO_MAIL_TO"
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail
#set the following line tothe path of the file
#NOTE: you can write click and copy path from the Raspi File Manager
attach_file_name = 'PUT PATH AND FILE NAME YOU WANT TO ATTACH HERE'
message.attach(MIMEText(mail_content, 'plain'))
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
#payload.set_payload((attach_file).read())
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
#payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
#message.attach(attach_file_name,maintype='image')
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address,sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
#to send more than one email
#session.sendmail(sender_address, receiver_address.split(","), text)
session.quit()
print('Mail Sent')