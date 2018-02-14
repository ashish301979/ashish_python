#!/usr/bin/python
import multiprocessing,sys
y=sys.argv[1]

#count=3 =>>>Issue with this
count=10000
c,b=[],[]
v=len(open("ashish_file1.txt").readlines())
def val(i):
y=sys.argv[1]
try:
a = "".join(open("ashish_file1.txt").readlines()[i:i+count])
for value in list(a.splitlines()):
if y in value.split() and value not in c:
c.append(value)
c.append("\n")
return "".join(c)
except ValueError:
return None

pool=multiprocessing.Pool(processes=4)
results=pool.map(val,range(0,v,count))
pool.close()
p=(results)
print("".join(set(p)))
