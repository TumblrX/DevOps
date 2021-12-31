import os
import psutil
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_main(receiver_addresses,subject,content):
	mail_content = content
	#The mail addresses and password
	sender_address = 'hmoairobot@gmail.com'
	sender_pass = 'mohamed3102000'
	receiver_address = receiver_addresses
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['Subject'] = subject
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	for receiver in receiver_address:
		message['To'] = receiver
		session.sendmail(sender_address, receiver, text)
	session.quit()
#-------------------------------------------
load1, load5, load15 = psutil.getloadavg()
  
cpu_usage = (load15/os.cpu_count()) * 100
  
if (cpu_usage>80):
	receiver_addresses = ['mohamedmiogh2@gmail.com','robertmounir66@gmail.com']
	content = '''The master server has reached the limit of 80 persent of CPU usage'''
	subject= 'Monitoring issue(master)'
	send_main(receiver_addresses,subject,content)