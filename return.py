def abc():
	#return [x for x in range(1, 10) if x > 2]
	for i in range(10):
		yield i*i
for value in abc():
	print(value)	
