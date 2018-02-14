'''def func():
    return 1,2,3
(a,b)=func()
======
class A(object):
    def calc(self):
        return 7
class B(object):
    def calc(self):
        return 6
class C(A,B):
    pass
c=C()
print c.calc()
========

import random
def fun(type_='s'):
    if type_=='s':
        return 'Mark'
    elif type_=='i':
        return random.randint(0,1000)
def dec(fun,type_):
    x=8
    def wrapper():
        value=fun(type_)
        if isinstance(value,int):
            return value*x
        elif isinstance(value,basestring):
            return 'Hi ' + value
        return wrapper()
    print dec(fun,'i')()


a=[1,2]
b=a
a=[3,4]
print b

class Org(object):
    __emp=[]
google=Org()
google.__emp.append(1)

import re
test="abc\r\ndo not have \r\n"
print "\n".join(re.split(r"\r\n", test))
print re.sub(r"(\r\n)", "\n", test)


data =[1,2,3,4,5,6]
print map(lambda r: r*3, filter(lambda f: f>3 or 0, data))
#print [3*i for i in data if i>3 else 0]
print [3*i for i in data if i >3]


r="p"
print ("T" if r == "p" else "F")   

print [l for l in open("abc") if l.startswith("ashish")]

list=[-1,2,-3]
print sorted(list, key=abs)

v=[(1,2),(3,4),(5,6),(7,8),(9,10)]
a = [x for y in v for x in y if x%2 == 0]
for value in a:
    print value
print a

def fab(n):
    list=[0,1]
    while len(list) < n:
        list.append(list[-1]+list[-2])  
    return list    
print fab(7)

def test(x):
    print x
    if x > 25:
        return x
    return test(2*x+1)
print test(20)

class CM(object):
    def __enter__(self):
        print "Rais IO E 1"
        raise IOError()
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        print "exiting"
        return False
c=CM()

with c:
    try:
        print "Rais IO E 2"
        raise ValueError()
    except ValueError:
        print "T C"

def sq(x):
    return x*x
def rec_map(func, seq):
    if seq==[]:
        return seq
    else:
        return [func(seq[0])] + rec_map(func, seq[1:])
print rec_map(sq, [1,2,3])
def rec_m(func, seq):
    if seq==[]:
        return seq
    else:
        return [rec_m(func, seq[1:])]
print rec_m(sq, [1,2,3])

if False:
    print "hi"
elif True:
    print "xx"
else:
    print "hh"   
    
name ='p'
while bool(name)==False:

def abc(*sss):
    print type(sss)
abc(1,2,3,4) 

a=range(5)
b=range(9)
print zip(a,b)    

def add(list):
    list+=[1]
list=[1,2,3,4]
add(list)
print len(list)
print list

a=[1,2]
b=[3,4]
c=9
t=(a,b,c)
print t
print type(t)
print hex(id(a))
print hex(id(c))
a.append(4)
c+=10
print t
print hex(id(a))
print hex(id(c))

t=([1, 2], [3, 4],9)
for i in t:
    if type(i)==list:
        i.append(9)
        print hex(id(i))
    else:
        i+=9
        print i
print t

import sys
class Abc():
    def __init__(self,v):
        self.v=v
    def ashish(self):
        for i in open(self.v):
            if "a" in i or "ABC" in i:
                print i.strip()
a=Abc("abc")
print a.ashish()

a=[9,4,1,3,7,2,8,1]
c=[]

def ashish(a):
    for i in range(len(a)):
        if a[0] > a[i]:
            a[0],a[i]=a[i],a[0]
    c.append(a.pop(0))
    if len(a) > 0:
        ashish(a)
ashish(a)
print c

a=[9,4,1,3,7,2,8,1]
c=[]
class Ashish():
    def __init__(self, value):
        self.value=value
    def ashish(self):
        for i in range(len(self.value)):
            if self.value[0] > self.value[i]:
                self.value[0],self.value[i]=self.value[i],self.value[0]
        c.append(self.value.pop(0))
        
b=Ashish(a)
for i in range(len(a)):
    b.ashish()
print c   

a=10
def ashish():
    global a
    print a
    a=1   
    print a 
ashish()   

#open("abc_out", "w+")
open("abc_error", "w+")
import sys
tmp=sys.stdout
sys.stderr=open("abc_error", 'a')
sys.stdout=open("abc_out", "w+")
for i in open("abc"):
    print i.strip() 
print tmp.read()

sys.stdout=tmp

a=[9,4,1,3,7,2,8,1]
c=[]

def ashish(a):
    for i in range(len(a)):
        if a[0] > a[i]:
            a[0],a[i]=a[i],a[0]
    c.append(a.pop(0))
    if len(a) > 0:
        return ashish(a)
    else:
        return c    
print ashish(a)

a=[9,4,1,3,7,2,8,1]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i],a[j]=a[j],a[i]
print a 

#re.search(<string to match>, <string in where to match>, re.I)
import sys,re
for i in open("abc"):
    if re.search("a",i.strip(), re.I):
        print i.strip()

a=3
c=[1,2]
b=a
print hex(id(a))
a+=1
print repr(a)
print hex(id(a))
print hex(id(b))
print hex(id(c))
c.append(4)
print hex(id(c))
print b

def deco_fun(original_fun):
    def first_fun(*args, **kwargs):
        print "Hello"
        return original_fun(*args, **kwargs)
    return first_fun
@deco_fun
def display(name):
    print "decorator Example"
    print name
display('ashis')   

def fun_1(fun2):
    print "checking"
    def fun_inner():
        print "checking inner fun"
        return fun2()
    return fun_inner()
@fun_1
def fun2():
    print "abc"

class A(object):
    def __init__(self,a):
        self.x=a
    def abc(self,b):
        print self.x**b
a=A(2)
a.abc(3)

class a:
    b="hello"
    c="n"
    @classmethod
    def abc(b):
        print b.b
        print b.c
    print dir(abc)
        
x=a()
x.abc()

print dir(x)

class A:
    c=4
    b=5
    @classmethod
    def bb(self):
        print self.c 
        print self.b
a=A()
a.bb()  

def abc():
    a=4
    b=5
    def c():
        print a,b
    c()          

abc()
  '''
   
        
        