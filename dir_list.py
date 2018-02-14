#!/usr/bin/python
import os
def di_list(y):
	for i in os.listdir(y):
		if os.path.isdir(os.path.join(y,i)):
			di_list(os.path.join(y,i))
		else:
			print os.path.join(y,i)
di_list("/etc")	
