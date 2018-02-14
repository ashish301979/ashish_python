import os,sys
def dhruv(y):
	for i in os.listdir(y):
		if os.path.isfile(y+"/"+i):
			print y+"/"+i,
			print os.path.getsize(y+"/"+i)
		else:
			dhruv(y+"/"+i)
dhruv(sys.argv[1])
		
	
