#!/usr/bin/python
h={}
li=['a','b','c','d','c','c','b','c','a']
for l in li:
	if l not in h.keys():
		h[l] = 1
	else:
		h[l] +=1
list=h.values()
for i in list:
	if list[0] < i:
		list[0]=i
for k,v in h.items():
	if h[k] == list[0]:print k, v
