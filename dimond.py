#!/usr/bin/python
def aa(y):
	j=1
	for i in range(1,y+1):
		if j <= 5:
			a_i=str("*"*j).rjust(y+i)
			j+=2
		print a_i
aa(5)
