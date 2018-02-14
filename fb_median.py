#!/usr/bin/python
list=['3', '5', '7', '12', '13', '14', '21', '23', '23', '23', '23', '29', '40', '56']
list1=sorted(list)
length=len(list1)
if length//2 != 0:
	print(list1[len(list)/2])
else:
	print((list1[(len(list)/2)-1] + list1[(len(list)/2)])/2)
