#!/usr/bin/python
import sys
import os
file2=open("abc").readlines()
print(len(sys.argv))
for value in any(x for x in range(1,len(sys.argv)+1) for x in file2):
	print(value)
