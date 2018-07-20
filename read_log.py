import ssh
import paramiko
import datetime
import smtplib
import stat
import time

logdata_traccar_server=[]
logdata_traccar_wrapper=[]
logdata_sqlerror=[]
timestr = time.strftime("%Y%m%d")
ssh_client = paramiko.SSHClient()
hostname = "159.89.170.250"
username=""
password=""
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname,22,username,password)
sftp_client = ssh_client.open_sftp()

# Read Traccar Server Log
remote_file = sftp_client.open('/opt/traccar/logs/tracker-server.log')
try:
    for line in remote_file:
        if 'WARN'in line:
            if 'Geocoding failed ' not in line :
                if 'Empty address' not in line :
                    logdata_traccar_server.append(line)
        elif 'ERROR'in line:
            logdata_traccar_server.append(line)
            print len(logdata)
        
finally:
        remote_file.close()

remote_file.close()

# Read Traccar Wrapper Log
try :
    remote_file = sftp_client.open('/opt/traccar/logs/'+'wrapper.log.'+(timestr))
    try:
        for line in remote_file:
            logdata_traccar_wrapper.append(line)
            
    finally:
        remote_file.close()
    remote_file.close()
except IOError :
    print "going good"

# Read SQL error Log
remote_file = sftp_client.open('/var/log/mysql/mysql_error.log')
try:
    for line in remote_file:
        logdata_sqlerror.append(line)
        
finally:
        remote_file.close()

remote_file.close()

print " Serever - Erros "
print len(logdata_traccar_server)

print " Wrapper - Erros "
print len(logdata_traccar_wrapper)

print "Database - Erros "
print len(logdata_sqlerror)


fromaddr = 'admin@intracworks.com'
toaddrs  = 'lnsvas@gmail.com','sripadalns@gmail.com','prabu38@gmail.com'
if ((len(logdata_traccar_server)) > 0) and ((len(logdata_traccar_wrapper)) > 0) and ((len(logdata_sqlerror)) > 0) :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Server Error are .... ",
      str((logdata_traccar_server)),
      " Wrapper Error are .... ",
      str((logdata_traccar_wrapper)),
      " Database Error are .... ",
      str((logdata_sqlerror))
  
      ])
elif ((len(logdata_traccar_server)) > 0) and ((len(logdata_traccar_wrapper)) > 0) and ((len(logdata_sqlerror)) == 0)  :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Server Error are .... ",
      str((logdata_traccar_server)),
      " Wrapper Error are .... ",
      str((logdata_traccar_wrapper))
 
      ])
elif ((len(logdata_traccar_server)) > 0) and ((len(logdata_traccar_wrapper)) == 0) and ((len(logdata_sqlerror)) > 0)  :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Server Error are .... ",
      str((logdata_traccar_server)),
      " Database Error are .... ",
      str((logdata_sqlerror))
  
      ])
elif ((len(logdata_traccar_server)) > 0) and ((len(logdata_traccar_wrapper)) == 0) and ((len(logdata_sqlerror)) == 0) :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Server Error are .... ",
      str((logdata_traccar_server))

  
      ])
elif ((len(logdata_traccar_server)) == 0) and ((len(logdata_traccar_wrapper)) > 0) and ((len(logdata_sqlerror)) > 0) :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Wrapper Error are .... ",
      str((logdata_traccar_wrapper)),
      " Database Error are .... ",
      str((logdata_sqlerror))
  
      ])
elif ((len(logdata_traccar_server)) == 0) and ((len(logdata_traccar_wrapper)) == 0) and ((len(logdata_sqlerror)) > 0) :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Database Error are .... ",
      str((logdata_sqlerror))
  
      ])
elif ((len(logdata_traccar_server)) == 0) and ((len(logdata_traccar_wrapper)) > 0) and ((len(logdata_sqlerror)) == 0) :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Server Errors",
      str(len(logdata_traccar_server)),
      "Wrapper Errors",
      str(len(logdata_traccar_wrapper)),
      "Database Errors",
      str(len(logdata_sqlerror)),
      " Wrapper Error are .... ",
      str((logdata_traccar_wrapper)),
      ])

else :
    msg = "\r\n".join([
      "Subject: Today's Serever Health",
      "Great !!! No Errors ",
      ])
print msg
username = ''
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()


