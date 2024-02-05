import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#for send IP
import socket
import fcntl
import struct

email_user = "my_sacrifical@gmail.com"
email_password = "my_sf_password"
email_send = "EMAIL_2B_NOTIFIED"


#create function to get ip address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',bytes(ifname[:15],'utf-8')))[20:24])    

#assign IP address to variable address
address = get_ip_address('wlan0')

subject=str(address)

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_send
msg["Subject"] = subject

body="The new IP address is " + str(address)

msg.attach(MIMEText(body,"plain"))
text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()
