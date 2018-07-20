import ssh
import paramiko
import datetime
import smtplib
ssh = paramiko.SSHClient()
hostname = "159.89.170.250"
username="root"
password="sripals$38205_$"
command ="df -h"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x= ssh.connect(hostname,22,username,password)
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
x= stdout.read()


text_file = open("Output.txt", "a")
datex = str(datetime.date.today())
text_file.write(datex)
text_file.write("\n")
timex=str(datetime.datetime.now().time())
text_file.write(timex)
text_file.write("\n")
text_file.write(x)
text_file.write("***********************\n")

text_file.close()


fromaddr = 'admin@intracworks.com'
toaddrs  = 'lnsvas@gmail.com','sripadalns@gmail.com','prabu38@gmail.com','pourni1990@gmail.com '
msg = "\r\n".join([
  "To: lnsvas@gmail.com",
  "Subject: Today's Serever Health",
  "",
  "None should be 100%",
  str(x)
  ])
username = 'info@intracworks.com'
password = 'awesomesupport@ITW'


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
