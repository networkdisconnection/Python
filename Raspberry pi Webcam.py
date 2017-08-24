import smtplib
import os
import time
import subprocess
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import RPi.GPIO as GPIO


strFrom = '@gmail.com'
strTo = '@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'subject'
msg['From'] = strFrom
msg['To'] = strTo

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
print "press button "


# Loop until users quits
while True:
input=GPIO.input(17)
        if input == True:
                print "Ready"
                subprocess.Popen(["fswebcam","-r 720x480", "test.jpg"])
                time.sleep(2)
                fp=open('test.jpg','rb')
                msgImage = MIMEImage(fp.read())
                msgImage = MIMEImage(fp.read())
                fp.close()


                msgRoot.set_payload(msImage)
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login('@gmail.com' , 'password')
                server.sendmail(strFrom, strTo,msg.as_string())
                server.close()
                print "send"