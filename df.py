#!/usr/bin/python
import os,sys,smtplib
list=[]
from email.mime.text import MIMEText

from subprocess import Popen, PIPE
file1=os.popen('df -hP').readlines()
for line in file1:
	if "filesystem" not in line.lower() and int(line.split()[-2].split("%")[0]) > 50:
		list.append(line.split()[-1].ljust(10) + "   :   "+ line.split()[-2])
final="\n".join(list)
msg = MIMEText(final)
print msg
From = "root@localhost"
To = "ashish301979@gmail.com"
if len(final) > 1:
	s = smtplib.SMTP('mail.127.0.0.1', 25)
	s.sendmail(From, To, msg.as_string())
	s.quit()
