import sys
fh=open("test_log")
#for line in fh:
#	if line.find('Filesystem') == -1:
#		continue
#	print line
fh.seek(0,2)
print fh.readline()
