#!/usr/bin/python
hash={}
list=['3', '5', '7', '12', '13', '14', '21', '23', '23', '23', '23', '29', '40', '56']
for i in list:
	if i not in hash.keys():
		hash[i] = 1
	else:
		hash[i] +=1
b=sorted(hash.items(), key=lambda x: x[1],reverse=True)[0][1]
for a in list:
	if a in hash.keys() and hash[a] == b:
		print a
		break
