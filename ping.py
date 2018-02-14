import os,threading,sys
b=[]
a="localhost"
def ping_test(a):
	print os.popen("ping  -c 1 " + a).readlines()
for i in range(5000):
	i=threading.Thread(target=ping_test, args=(a,))
	b.append(i)
	i.start()
for j in b:
	j.join()

