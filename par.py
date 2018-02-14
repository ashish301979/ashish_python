#!/usr/bin/python
import multiprocessing,sys
count=len(open("/var/log/system.log").readlines())/2
print(count)
print(count*2)
def ash(y):
	a=[]
	for value in "\n".join(open("/var/log/system.log").readlines(y)).split("\n")[0:]: 
		a.append(value.strip())
	return "\n".join(a)
pool=multiprocessing.Pool(processes=2)
result=pool.map(ash,range(0,count*2,count))
pool.close()
print(result)
