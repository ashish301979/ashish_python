import sys
k=50000
j=300
file=open(sys.argv[1], 'r')
for i in range(70):
	file.seek(k)
	open("ashish_write", 'a+').write(file.read(j))
	k+=j
	print k
	print "+++++++++++++++++++"
	open("ashish_write", 'a+').close()
