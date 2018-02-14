import time,datetime
a=datetime.datetime.now()-datetime.timedelta(minutes=1200)
b=a.strftime("%b %d %H:%M:%S")
for i in open("/var/log/system.log"):
	if len(i.split())>3 and i.split()[0:3] > b:
		print i
