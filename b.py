#/usr/bin/python
import multiprocessing,sys

ran=1
b=len(sys.argv)
def fuy(u):
	return open(sys.argv[u]).read()
for v in range(b-1):	
	print(fuy(v+1))
