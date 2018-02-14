list=['a','b','c','d','abcd','h','a','b','c','d','h','l']
'''

for i in range(len(list)):
	if len(str(list[0])) < len(str(list[i])):
		list[0] = list[i]
		
print list[0]
		
'''
for i in range(0,len(list)):
	list[0],list[i] = list[i],list[0]
	if list[0] not in list[1:]:
		print list[0]
		break
