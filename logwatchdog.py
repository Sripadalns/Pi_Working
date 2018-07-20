import paramiko
import string

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('159.89.170.250', username='', password='') 
    
ftp = ssh.open_sftp()
file=ftp.file('/var/log/mysql/mysql_error.log', "r", -1)
data=file.read()
L = string.split(data)
for i in L:
    if string.find(i, '%')>-1:
        print i
    print ftp.stat("/var/log/mysql/mysql_error.log")        
    ftp.close()
    print "DONE!"   
else: 
    print "EXIT!"
ssh.close()
