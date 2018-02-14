'''def abc_list():
    list=open("abc").readlines()
    t=0
    num=0
    while num < len(list):
        b=list[num]
        a=b.rsplit(None,1)[1]
        yield int(a)
        num+=1
print sum(abc_list())

class A(object):
    def __repr__(self):
        return 'instance of A'
a=A()
b=a
del a
print b

map =7 
print map

def fun():
    return 1,2,3
(a,b)=fun()
class A:
    pass
class B:
    pass
a=A()
b=B()
print type(a)==type(b), type(a),type(b)

class Organization(object):
    __employees=[]
google=Organization()
google.__employee.append('Erick')

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"

import random
def func(type_='s'):
    if type_=='s':
        return 'mark'
    elif type_=='i':
        return random.randint(0,100)
def dec(func, type_):
    x=8
    def wrapper():
        value=func(type_)
        if isinstance(value, int):
            return value *x
        elif isinstance(value, basestring):
            return 'Hi + value'
        return wrapper
print dec(func, 'i')()    

a=[1,2,3]
b=a
a=[5]
print b

class A(object):
    def __repr__(self):
        return 'instance of A'
a=A()
b=a
del a
print b

def func():
    return 1,2,3
(a,b)=func()

class Org(object):
    __emp=[]
google=Org()
google.__emp.append('Eric')

=============

mul=8
a=lambda x, y: (x* mul) / y
print a(2,3)

import copy
class A(object):
    pass
a=A()
a.lst=[1,2,3]
a.str='cats and dogs'
b=copy.copy(a)
a.lst.append(100)
a.str='cats ans mice'
print b.lst
print b.str

===============
import datetime
from numpy.distutils.fcompiler import none
class Human(object):
    name=None
    gender=None
    birthdate=None
def __getattr__(self, name):
    if name == 'age':
        return datetime.datetime.now() - self.birthdate
    else:
        return None
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
h=Human()
h.birthdate= datetime.datetime(1984, 8, 20)
h.age=28
print h.age   
=====================
class Human(object):
    def __setattr__(self, name, value):
        if name == 'gender':
            if value in ('male', 'female'):
                self.gender=value
            else:
                raise AttributeError(' g can be m or f')
h=Human()
h.name='Mary'
h.gender='female'
print h.gender
=====================
class A:
    brothers=[]
    def __init__(self, name):
        self.name=name
        
a=A('Rich')
b=A('Elly')
a.brothers.append('john')
print a.name, a.brothers,b.name,b.brothers
def add(x):
    return x+x
a=map(add, [1,2,3])
print a       
'''