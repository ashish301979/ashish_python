#!/usr/bin/python
start=4
end=15
def fn(start):
	if start < 2:
		return start
	else:
		return fn(start-1) + fn(start-2)
for i in range(start,end):
	print(fn(i))
	
	
