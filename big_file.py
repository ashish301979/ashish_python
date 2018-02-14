fh=open("ashish_log1")
fh.seek(-600,2)
for i in fh:
	print i
