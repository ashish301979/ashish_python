#!/usr/bin/python
f1=open("ashish_passwd").readlines()
print(type(f1))
for x in sorted(f1, key=lambda x: x.split(":")[2]):
	print(x)
