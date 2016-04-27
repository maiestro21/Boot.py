import smtplib
import base64
import time

def sendMail( toMail, message, subject):
   
	fromaddr = 'From: <#your-email@gmail.com#>'
	toaddrs  = toMail
	msg = 'Subject: %s\n\n%s' % (subject, message)
	


	# date cont
	username = "#your-email@gmail.com#"
	password = base64.b64decode('#Your base64 encoded password#')

	# smtp google
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	return

#reading creds
mailTo = "#Destination email#"
subjectTo = "DEVICE01 STARTED AT: " + " " + time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
message = time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
sendMail(mailTo, message, subjectTo)



  
 

