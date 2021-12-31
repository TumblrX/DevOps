from flask import Flask, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

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
#---------------------------
resived=False
def com_routine():
	global resived
	if(not(resived)):
		print('No resiver mail sent.')
		receiver_addresses = ['mohamedmiogh2@gmail.com']
		content = '''I did't rescive a meesage from slave for some time now.'''
		subject= 'Monitoring issue'
		send_main(receiver_addresses,subject,content)
	resived=False


scheduler = BackgroundScheduler()
scheduler.add_job(func=com_routine, trigger="interval", seconds=130)
scheduler.start()
#---------------------------
app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
	global resived
	#print(request.form['me']) # should display 'mario'
	resived=True
	return 'Received !' # response to your request.

app.run(host='0.0.0.0', port=1234)
#-----------------------------------
atexit.register(lambda: scheduler.shutdown())
