#!/usr/bin/python
#Ashish Singh
string1="ashisi"
string2="helloashish"
count=0
for i in string1:
	for j in string2:
		if i != j:
			continue
		else:
			l=0
			while string1[string1.index(i)+l] == string2[string2.index(j)+l]:
				l +=1
		if count < l:		
			count=l
print count

'''x = "ashisi"
y="helloashish" 
if len(x) <= len(y):
  x,y = y,x
count = 0
for i in range(0,len(x)):
  for j in range(0,len(y)):
    if x[i] != y[j]:
      continue
    else:
      k = 0
      while (i+k) < len(x) and (j+k) < len(y) and x[i+k] == y[j+k]:
        k += 1
    if count < k:
      count = k
print count'''
