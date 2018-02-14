#!/usr/bin/python
import sys,re
f=open("test_log").readlines()
replace=re.compile('(\.|_)')
f2=replace.sub(" ", f)
h={}
for line in f2:
	if len(line) > 0:
		line.split()[0:2] not in h.keys()
		h[str(line.split()[0:2])] = str(line.split()[2:])
		print str(line.split()[0:2])
