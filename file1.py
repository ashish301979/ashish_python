#!/usr/bin/python
import sys
f=open("file1").readlines()
h={}
for v in f:
	if v.split()[0] not in h.keys():
		h[v.split()[0]] = " ".join(v.split()[1:])
		h[v.split()[0]] += " "
	else:
		h[v.split()[0]] += " ".join(v.split()[1:])
var=sys.argv[1].lower().strip()
if var in h.keys():
	print var, " : ", h[var] 
