#!/usr/bin/python
import os,sys

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
def dir_rec(y):
	for i in os.listdir(y):
		a=os.path.join(y,i)
		if os.path.isdir(a):
			dir_rec(a)
		else:
			#print a.ljust(40),convert_bytes(os.stat(a).st_size)
			print a.ljust(40),convert_bytes(os.path.getsize(a))
	
dir_rec(sys.argv[1])
