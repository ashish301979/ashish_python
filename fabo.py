#!/usr/bin/python
def fn1(y):
	if y <2:
		return y
	else:
		return fn1(y-1)+fn1(y-2)
i=1
sum=0
sum1=0
while sum <= 4000000:
	sum +=fn1(i)
	if sum <= 4000000:
		if fn1(i)%2 == 0:
			sum1 +=fn1(i)
		i+=1
print sum1

	
