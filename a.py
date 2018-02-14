#/usr/bin/python
import multiprocessing,sys

ran=1
b=len(sys.argv)
def fuy(u):
	return open(sys.argv[u]).read()
	
pool=multiprocessing.Pool(processes=4)
result=pool.map(fuy,range(1,b,ran))
pool.close()
print(result)
