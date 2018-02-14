#!/usr/bin/python
f1,f2=0,1
def febo():
	i=0
	f1,f2=0,1
	while i< 10:
		print(f2)
		f1,f2=f2, f1+f2
		i+=1
febo()
