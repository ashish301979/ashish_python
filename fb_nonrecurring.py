#!/usr/bin/python
hash={}
list=['3', '5', '7', '12', '13', '14', '21', '23', '23', '23', '23', '29', '40', '56']
for i in list:
	if i not in hash.keys():
		hash[i] = 1
	else:
		hash[i] +=1
for a in list:
	if a in hash.keys() and hash[a] == 1:
		print a
		break
