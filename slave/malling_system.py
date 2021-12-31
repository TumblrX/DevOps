import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def check_current_val(image_name):
	result = subprocess.run(['docker','inspect',"--format='{{index .RepoDigests 0}}'",image_name], stdout=subprocess.PIPE)
	result = result.stdout.decode('utf-8')
	x = re.findall("sha256:.*", result)
	x=x[0]
	x=x[0:len(x)-1]
	return x

def check_online_val(image_name):
	result = subprocess.run(['docker','pull',image_name], stdout=subprocess.PIPE)
	result = result.stdout.decode('utf-8')
	x = re.findall("sha256:.*", result)
	x=x[0]
	return x

def is_changed(image_name):
	x1=check_current_val(image_name)
	x2=check_online_val(image_name)
	return x1!=x2

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
#---------------------------------------------------------
changed=False

if(is_changed('muhammad2000/front')):
	receiver_addresses = ['mohamedmiogh2@gmail.com','15126@stemegypt.edu.eg']
	content = '''The code front team has pushed has deployed and it is now up'''
	subject= 'Deployment'
	send_main(receiver_addresses,subject,content)
	changed=True

if(is_changed('muhammad2000/back')):
	receiver_addresses = ['mohamedmiogh2@gmail.com','bishoyatef313@gmail.com']
	content = '''The code back team has pushed has deployed and it is now up'''
	subject= 'Deployment'
	send_main(receiver_addresses,subject,content)
	changed=True

if(is_changed('muhammad2000/cross')):
	receiver_addresses = ['mohamedmiogh2@gmail.com','ammarmohamed13@gmail.com']
	content = '''The code cross team has pushed has deployed (web) and it is now up'''
	subject= 'Deployment'
	send_main(receiver_addresses,subject,content)
	changed=True

if(changed):
	result = subprocess.run(['sh','/home/slave/project/rst.sh'], stdout=subprocess.PIPE)
	changed=False