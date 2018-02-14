'''import copy
class A(object):
    pass
a=A()
a.list=[1,2,3]
b=copy.copy(a)
c=a
print a.list
a.list.append(4)
print b.list
print c.list
print dir(a)

a=[1,2,3,4,5,6,7]
print a.__sizeof__()
print tuple(a).__sizeof__()
for i in tuple(a):
    print i
print a
print id(a) 
a[0]=5
print id(a)

import re
b="AShishhh"
if re.search("a", b,re.I):
    print b   

class A():
    def abc(self):
        print id(self)
    def b(self):
        print id(self)
a=A()
print id(a)
a.abc()
a.b()

import logging
logging.basicConfig(filename="ashish_log")
try:
    a=(1,2,3,4)
    print a
    print dict(a)  
    print a 
except:
    print "error"           
def ash():
    mes="abc"
    def a():
        print mes
    return a()
ash() 

import sys
def ash(*args):
    x=sys.argv[0]
    def a():
        print x
    return a
print id(ash())        
b=ash()
print id(b)
c=ash()
print id(c)     
d=ash()
print id(d)
del ash
c()  
b()
d()

class A():
    def a(self):
        
        print "s"
b=A()
b.a()   
print id(b)
b.c="hello"
print b.c
print id(b)
print b.a()     

a=[]
b=a
print hex(id(a))
print hex(id(b))
b.append(1)
print hex(id(b))
print b
print a
a.insert(2,2)
a.insert(2,2)
a.insert(2,2)
a.insert(1,5)

print a

total=15000000
for i in range(1,31):
    total=total+total*4/100
print total

Total_Money=15000000                                        
Intrest_Earned=Total_Money*3/100    
counter=0
                                    
for i in range(1,31): 
    Intrest_Earned=Total_Money*3/100                       
    if i <= 10:
        print "Member",i, "will get ",225000
        Total_Money=Total_Money+Intrest_Earned-225000
    elif i >10 and i<=20:
        print "Member",i, "will get ",275000
        Total_Money=Total_Money+Intrest_Earned-275000
    else:
        print "Member",i, "will get ",350000
        Total_Money=Total_Money+Intrest_Earned-350000
            
print Total_Money                                               
print "Profit :",Total_Money - 300000*70

def ab():
    for i in open("abc"):
        yield i
    
def fun(x):
    return x + x
for j in map(fun,ab()):
    print j,

class abc():
    @classmethod
    def a(cls):
        print cls
abc().a()     

import re
a="ABCDEDCBa"
re.I(a)

h={}
for line in open("abc"):
    if line.split().pop(-1) not in h.keys():
        new=line.split()
        a=[]
        key=new.pop(-1)
        a.append(" ".join(new))
    else:
        a.append(new)    
    h[key]=a
for k,v in h.items():
    print k,
    print "\t : "+"".join(v)  

def ashish(a=[]):
    a.append(1)
    print a
ashish()
ashish()
ashish()

def ashish(x):
    print x*x
map(ashish,[1,2,3,4,5,6,7,8,9])  

def f(x):
    return x%2 !=0 and x%3 !=0
result=filter(f, range(1,20))
print result
"hello Tecxt is text".strip('Te')

def ash():
    import string
    a='apczd'
    b=[]
    for i,j in enumerate(string.ascii_lowercase):
        for k in a:
            if k == j:
                b.append(k+str(i))
    new=''            
    for i in sorted(b, key=lambda x: x[0]):
        new+=i[0]  
    return new       
print ash() 
  
def LetterChanges(str): 
    import string
    b='aeiou'
    for i,j in enumerate(string.ascii_lowercase):
        for k in str:
            if k == j and string.ascii_lowercase[i+1] in b:
                str=str.replace(string.ascii_lowercase[i+1].upper())
            else:
                str=str.replace(string.ascii_lowercase[i+1])
    return str            
    
# keep this function call here  
print LetterChanges('ashish')

def LetterChanges(str): 
    import string
    str1=str[:]
    str2=str[:]
    for i,j in enumerate(string.ascii_lowercase):
        if j in str2 and len(string.ascii_lowercase)  > i+1:
            a=string.replace(str,j,string.ascii_lowercase[i+1])
            str=a
            str2=string.replace(str1,j,'')
    return str            
# keep this function call here  
print LetterChanges('ashish')

def ashish():
    import string
    str=''
    a='bc'
    a=string.replace(a,'b','z')
    d=a
    print id(d)
    print id(a)
    a=string.replace(a,'c','z')
    print id(d)
    print id(a)
ashish()

def test(x,y):
    #x=input("Enter the First number : ")
    #y=input("Enter the Second Number : ")
    for i in (range(x,y+1)):    
        if len(str(i)) < 2 and i ==7:
            print "Number has 7 : ",i
        else:
            a=0
            for j in str(i):
                a+=int(j)   
                if a == 7:
                    print "Number have 7 : " , i ," : " ,a 
test(5,43)

def test():
    a=''
    x=input("Enter the First number : ")
    y=input("Enter the Second Number : ")
    for i in (range(x,y+1)):
        if len(str(i)) < 2:   
             a+=str(i)+"+"
        else:
            for j in str(i):
                a+=str(j)+"+"     
    print a         
test()                            

import os,re,sys
#fh=open("/var/tmp/ashish_test", 'w+')
def re_ashish(x):
    for i in os.listdir(x):
        new_value=x+"/"+i  
        if os.path.islink(new_value):
            pass 
            
        elif os.path.isfile(new_value):
            #fh.write("/etc/"+i) 
            print new_value     
        else:
            re_ashish(new_value)
re_ashish("/etc")

import multiprocessing
import sys
v=9999
new=v
j=0
a=()
b=[]
for i in range(0,v,1000):
    if new > 1000:
        new=new-1000
        a=(j,1000+i)
        b.append(a)
        j+=1000
    else:
        a=(j,new+j)
        b.append(a)   
#count=3 =>>>Issue with this
count=10000
b=[]
c=[]
file1=open("abc")
def val(value1,value2):
    try:
        for line in open(file1).readlines()[value1:value2+1]:
            print line        
    except ValueError:
        return None
pool=multiprocessing.Pool(processes=4)
results=pool.map(val,[[x[0],x[1]] for x in b)
pool.close()
p=(results)
print("".join(set(p)))
#+++++++++++++++++
v=9999
new=v
j=0
a=()
b=[]
for i in range(0,v,1000):
    if new > 1000:
        new=new-1000
        a=(j,1000+i)
        b.append(a)
        j+=1000
    else:
        a=(j,new+j)
        b.append(a)
print b       

lt=[(1,2),(3,4),(5,6)]

def ab(*argv):
    v=argv[0][0]
    c=argv[0][1]
    return v
print map(ab,([[x[0],x[1]] for x in lt))  
    '''