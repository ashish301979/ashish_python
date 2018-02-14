#!/usr/bin/python
list = [123, 'xyz', 'zara', 'abc']
max=''
hash={}
count=0
a=0
for value in list:
	if len(hash.keys()) < 1:
		hash[value]=len(str(value))
	else:
		hash[value]=len(value)
print(sorted(hash.items(), key=lambda x: x[1], reverse=True)[0][1])
