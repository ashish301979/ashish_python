#!/usr/bin/python
def fn(y):
	if y < 2:
		return y
	else:
		return (fn(y-1) + fn(y-2))
for i in range(10):
	print(fn(i)) 
