import ssh
import paramiko
import datetime
import smtplib
import json
from Health_Device import *

ssh = paramiko.SSHClient()
hostname = "159.89.170.250"
username=""
password=""
command ="df -h"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x= ssh.connect(hostname,22,username,password)
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
y = stdout.read()
print y
with open("Output.json","w") as f:
  json.dump(y, f)

# reads it back
with open("Output.json","r") as f:
  d = json.load(f)


maxload = 100
stop = False
while (( maxload > 50 ) and (stop == False)):
    load = str(maxload)+'%'
    if (d.find(load) != -1):
        report = "Action Needed ! Server Load > 50% "
        stop = True
    else:
        report = "Server Going Good ! Have a great Day"
    maxload =maxload-1


cookie = login()
blist =get_device(cookie)

if ( len(blist) > 0) :
    device_report = " Below Devices are having problem . Offline for more than 24 Hours"
else:
    device_report = " All Devices are active. No action Needed. Good day to you !!!! "

  

fromaddr = 'admin@intracworks.com'
toaddrs  = 'lnsvas@gmail.com','sripadalns@gmail.com','prabu38@gmail.com','pourni1990@gmail.com ','pavan.bodapati@gmail.com' 
msg = "\r\n".join([
  "To: lnsvas@gmail.com",
  "Subject: Today's System Health",
  "",
  report,
  device_report,
  str(blist)
  ])

username = ''
password = ''


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
