import lock
a=
fh=open("file", 'r')
for i in fh:
	print fh.tell()
	print i
