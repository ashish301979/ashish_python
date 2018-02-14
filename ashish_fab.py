import sys
def ash_fab(y):
	list=[1]
	print "*".rjust(15)
	for i in range(y-2):
		list.append(list[-1]+1)
		print ("*"*(list[-2]+1)).rjust(15)
ash_fab(int(sys.argv[1]))

