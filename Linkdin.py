'''def ashish1():
    h={}
    v=[]
    a=''
    for value in open("lin_file2"):
        if len(value.strip())>0:
            v=1
            if a != ":".join(value.strip().split(":")[0:2]):
                a=":".join(value.strip().split(":")[0:2])
            else:
                v+=1
            h[a]=v  
    return h          
            
            
for k,v in sorted(ashish1().items(), key=lambda y: y[0]):
    print k,v 

class Shape(object):
    sides = 4

class Square(Shape):
    pass

class Triangle(Shape):
    pass

print (Shape.sides, Square.sides, Triangle.sides)
Triangle.sides = Triangle.sides - 1
print (Shape.sides, Square.sides, Triangle.sides)
Shape.sides = Square.sides + 2
print (Shape.sides, Square.sides, Triangle.sides)

import requests
r = requests.get('https://www.ndtv.com/')
print r.status_code
print r.headers['Content-Type']

print r.text

new_list=[]
lis=[1,3,5,6,2,3]
a=0
for i in lis:
    new_list.append(i)
    new_list.append(a+i)
    a=i
    
for i in range(1,list(set(sorted(new_list)))[-1]+2):
    if i not in new_list:
        print i
        break
    

lis=[1,2,2,5,7]
lis1=lis[:]
new_list=[]
j=0   
def ash(lis):
    j=0
    for i,y in enumerate(lis):
        a=lis1[i]
        new_list.append(a)
        new_list.append(y+a)
    
    if len(lis)>0:  
        del lis[0]
        return ash(lis)
ash(lis)
print list(set(new_list))
for i in range(1,list(set(sorted(new_list)))[-1]+2):
    if i not in new_list:
        print i
        break     
        
list=['a','b','c','d','e','f','g','h','i']
def ashish(list,x,y):
    if x > 0 and y < len(list):
        return list[0:x+1]+list[x:y+1][::-1]+list[y+1:]  
    else:
        return "some thing wrong with the argument passed"
print ashish(list,3,7)  

a=[1,2,3,4,5,6,7,0,5,6,7,8,9,0,4,0,5]   
for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)
print a 

list='abcabcdefgabcd'
for i in list.split():
    word=i
    list_count=list(map(word.count, word))
print list_count 

h={}
list='abcbdbfbgbsbabdbdsda'
for i in list:
    if i not in h.keys():
        h[i]=1
    else:
        h[i]+=1
print sorted(h.items(), key=lambda x: x[1])[-1]            
    

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        number=A
        j=0
        for i in number:
            if i != 0:
                j+=1
        return j
new_prog=Solution()
print new_prog.numSetBits('0001001010101010101')

def ashish():
    new_list=[]
    new_list1=[]
    h={}
    for values in [1,22,32,44,55,66,7,8,9,22,32,44,55]:
        new_list.append(str(bin(values)[2:].count("1"))+ " "+ str(values))    
    for i in sorted(new_list, key=lambda x:x[0]):
        if i.split()[0] not in h.keys():
            v=[]
            key=i.split()[0]
            v.append(int(i.split()[1]))
        else:
            v.append(int(i.split()[1])) 
        h[key]=v
    for i,k in sorted(h.items(), key=lambda x:x[0]):
        print i,sorted(k)
        new_list1+=sorted(k)          
    #new_list1.append(i.split()[1])
    return new_list1   
print ashish() 

import sys
def rearrange(elements):
    new_list=[]
    new_list1=[]
    h={}
    for values in elements:
        new_list.append(str(bin(int(values))[2:].count("1"))+ " "+ (values))    
    for i in sorted(new_list, key=lambda x:x[0]):
        if i.split()[0] not in h.keys():
            v=[]
            key=i.split()[0]
            v.append(int(i.split()[1]))
        else:
            v.append(int(i.split()[1])) 
        h[key]=v
    for i,k in sorted(h.items(), key=lambda x:x[0]):
        print i,sorted(k)
        new_list1+=sorted(k)          
    #new_list1.append(i.split()[1])
    return new_list1
def main():
    data = sys.stdin.readlines()
    
    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(data[i])

    result = rearrange(elements)
    
    for val in result:
        print(val)
main()


import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!

def rearrange(elements):
    bin1={}
    for j in elements:
        k = int(j)
        d = bin(k)[2:].count('1')
        bin1[k] = d
    final = []
    for i in range(1,max(bin1.values())+1):
        fin = []
        for keys in bin1:
            if bin1[keys] == i:
                fin.append(keys)
        final+=sorted(fin)
    return final


* DO NOT MODIFY CODE BELOW THIS POINT!

def main():
    data = sys.stdin.readlines()
     
    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(data[i])

    result = rearrange(elements)
    
    for val in result:
        print(val)

main()


import re
a="ashish"
print re.sub("h","",a,2)

a= [1,22,32,44,55,66,7,8,9,22,32,44,55]
new_list=[]
def ashish(a):
    for i in range(1,len(a)):
        if a[0] < a[i]:
            a[0],a[i]=a[i],a[0]
    new_list.append(a[0])        
    a.remove(a[0])
    if len(a) > 0:
        return ashish(a)
ashish(a)
print new_list

a= [1,22,32,44,55,66,7,8,9,22,32,44,55]
for i in range(1,len(a)):
    if a[0] < a[i]:
        a[i],a[0] = a[0],a[i]
        
    print a    
print a 

elements=[1,22,32,44,55,66,7,8,9,22,32,44,55]   
new_list1=[]
h={} 
for i in elements:
        h[i]=bin(i)[2:].count("1")  
for i in range(1,len(h)+1):
    new_list=[]      
    for keys in h:
        if h[keys] == i:
            new_list.append(keys)
    new_list1+=sorted(new_list) 
print new_list1    
 
j=0
fh=open("abc")

for value in range(10):
    i=value-j
    print fh.read(i+4)
    #print fh.tell()
    j+=1       
    
a='ashish'
b=len(a)-1
while b >= 0:
    print a[b],
    b-=1

elements=[1,22,32,44,55,66,7,8,9,22,32,44,55] 
new=[]
value=[]
for i in elements:
    new.append((i,bin(i)[2:].count('1')))
print new    
for i in sorted(sorted(new), key=lambda x: x[1]):
    value.append(i[0])
print value

a=set()
for i in open("abc"):
    a.add(i.strip())
print a 
for i in range(10,-1,-1):
    print i    

def multi():
    return (lambda x: i*x for i in range(4))
print [m(2) for m in multi()]

def extendList(val, list=[]):
    list.append(val)
    return list
list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')
print "list1=%s" % list1
print "list2=%s" % list2
print "list3=%s" %list3

list=[[1],[2]]*5
print list
list2=[1]*10
print list2
list[0].append(10)
print list
list[1].append(20)
print list
list.append(30)
print list

class DefaultDict(dict):
    def __missing__(self, key):
        return []
d=DefaultDict()
d['flop']=127
print d   

a='ashish'
print a[::-1] 

def ashish(b,a=10):
    print b
    print a
ashish(2,5)'

def solution(A):
   sum_t=sum(A)
   sum_b=A[0]
   sum_l=sum(A[1:])
   c=abs(sum_b-sum_l)
   for p in range(1,len(A)-1):
      
      if abs(sum_b+A[p] - sum_l-A[p]) < c:
            c=abs(sum_b+A[p] - sum_l-A[p])
      sum_b+=A[p]
      sum_l-=A[p]
   return c         
print solution([3,1,2,4,3])

def new_list(A):
    if len(A) == 0:
        return 1
    elif len(A)<2 and A[0] <2:
        return A[0]+1
    elif len(A) <2:
        return A[0]-1
    elif len(A) ==2 and abs(A[0]-A[1])==1:
        if sorted(A)[0] >1:
            return sorted(A)[0] -1    
        else:
            return A[1]+1 
    elif len(sorted(A))-1+sorted(A)[0] == sorted(A)[-1] and sorted(A)[0] <2:
        return sorted(A)[-1]+1   
    elif  len(sorted(A))-1+sorted(A)[0] == sorted(A)[-1] and sorted(A)[0] > 1:
        return A[0]-1
    else:
        a=sorted(A)
        b=a[-1] - a[0]
        c=a[0]
    
        for i in range(1,b+1):
            if c+1 != a[i]:
                return a[i]-1
                break
            else:
                c=a[i]
print new_list([1,2,3,4,5])   

def solution(A):
    if len(set(A)) != len(A):
        return 0
    elif sorted(set(A))[0]+len(set(A))-1==sorted(set(A))[-1] and sorted(set(A))[0]==1:
        return 1
    else:
        return 0
print solution([1,1])  

def ashish(x,A):
    
    a=0
    if len(A)-1>x:
        return -1
    else:
        for i in range(len(A)):
            if A[i] >= x:
                a=i
                break
            else:
                a=-1
    return a            
print ashish(1,[1]) 
print ashish(2, [2, 2, 2, 2, 2])  

def solution(A):
    c=set(sorted(A))
    y=[x for x in c if x > 0]
    b=0
    if len(y) == 0:
        b=1
    elif y[0]==y[-1]-(len(y)-1) and y[0] == 1:
        b=y[-1]+1
    elif y[-1] < 1:
        b=1    
    else: 
        for i in range(1,y[-1]):
            if i not in y[i]:
                b=i
                break
    return b           
print solution([-1,-3,1])  

def solution(A):
    c=set(sorted(A))
    y=[x for x in c if x > 0 and type(x) is int]
    b=0
    if len(y) == 0:
        b=1
    elif y[0]==y[-1]-(len(y)-1) and y[0] == 1:
        b=y[-1]+1
    elif y[-1] < 1:
        b=1    
    else: 
        for i in range(1,y[-1]):
            if i != y[i-1]:
                b=i
                break
    return b
print solution(['a','b','c', -1,1,2,3])               

def solution(A, B, K):
    new=0
    new1=[]
    y=[]
    l=[]
    n=[]
    if B-A > 5000:
        y=[x for x in range(A,B,5000)]
        if y[-1] < B:
            y.append(B+1)
        #print y    
        def hello(p):
            a=int(str(p).strip('[').strip(']').split(',')[0])
            b=int(str(p).strip('[').strip(']').split(',')[1])
            c=int(str(p).strip('[').strip(']').split(',')[2])
            
            for i in range(a,b+1):
                if i % c== 0:
                    new1.append(1)
        if len(y) > 0 :           
            b=[(y[x-1],y[x]) for x in range(1,len(y))] 
            for g in b:
                l.append(list(g))  
            for v in range(len(l)):
                k=l[v]
                k.append(K)
                n.append(str(k))       
        map(hello, n)           
        new=sum(new1)
    else:
        for i in range(A,B+1):
            if i % K == 0:
                new+=1     
    return new
print solution(100,123000000,2)
A=[1,2,3,4,5,6,7,8]
def solution(A):
    B=A[:]
    s=0
    l=1
    count = 1
    for i in range(len(B)):
        if B[s] > -1:
            while B[i] + B[l] > -1 and l < len(B)-2:
                if l < len(B)-2:
                    l+=1
                    s+=1  
                if count < l:
                    count =l 
        else :
            s+=1                
    return count           
print solution([1, 1, -1, -1, -1, -1, 1, 1])

def solution(N):
    import itertools
    A=list(str(N))
    M=len(A)
    counter =0
    x=list(itertools.permutations(A,M))
    for value in set(x):
        if '0' not in value[0] and len(set(x)) > 0:
            counter+=1
        elif len(set(x)) == 1: 
             counter =1
    return counter

def ashish(N):
    list1=list(str(N))
    list2=[]              
    for i in range(len(list1)):        
        list1[0],list1[-1]=list1[-1],list1[0] 
        list2.append("".join(list1))
    return len(list2)    
print ashish(12346)

def solution(A):
    cnt1 = 0
    cnt = 0
    sum2 = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            sum2 = sum(A[i:j+1])
            cnt1=len(A[i:j+1])
            if sum2 >= 0 and cnt1 >= cnt:
                cnt = cnt1
        sum2 = 0
        cnt1 = 0
    return cnt

def solution(A):
    s,a=0,[]
    for i in range(len(A)):
        s+=A[i]
        if s > -1:
            #a.append((i+1,s))
            a=i+1,s
    if len(a) < 1:
        return 0
    else:            
        return a[0]
print solution([1, 1, -1, -1,-1, -1, -1, 1, 1])

def solution(A):
    s,s1,a,b=0,0,[],0
    for i in range(len(A)):
        s+=A[i]
        if s > -1:
            a=i+1,s
        for j in range(i,len(A)):
            s1+=A[j]
            if s1>-1:
                a1=j+1,s1  
    if len(a) < 1 and len(a) > 0:
        return 0
    else:  
        if a[0] > a1[0]:
            b=a[0]
        else:
            b=a1[0]
    return b            
print solution([1, 1, -1, -1,-1, -1, -1, 1, 1])


n=[1,2,3,4,5,4,4,4,4,4]
print [j for i,j in enumerate(n) if i%2==0 and j%2==0]
print [x for x in n[::2] if x%2==0]
import itertools
a=[1,2,2,5,7]
print a
new=[]
new1=[]
for i in range(len(a)+1):
    for j in itertools.combinations(a,i):
        new.append(sum(j))
new1=new+a
for i in range(sorted(set(new1))[-1]+2):
    if i not in new1:
        print i   

header,value=[],[]
for line in open("file"):
    if "--" not in line:
        if line.split(":")[0] not in header:
            header.append(line.split(":")[0])
        value.append(line.split(":")[1].strip())    
print " ".join(header)
for i in range(0,len(value),3):
    print ' '.join(value[i:i+3])         

def ashish(list1):
    max_ending=max_sofar=0
    for i in range(0,len(list1)):
        max_ending=max_ending+list1[i]
        if max_ending < 0:
            max_ending=0
        if max_ending < max_sofar:
            max_sofar=max_ending
    return max_sofar       
print ashish([-1, 1, 1,-1, 1, 1])

def maxSubArraySum(a):
 
    max_so_far = 0
    max_ending_here = 0
    size=len(a)
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
print maxSubArraySum([-1, 1, 1,-1, 1, 1]) 

def maxSubArraySum(A):
    max_so_far = 0
    max_ending_here = 0
    size=len(A)
    j=[]
      
    for i in range(0, size):
        max_ending_here = max_ending_here + A[i]
        if max_ending_here > -1:
                print i
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            j.append((i,max_ending_here))
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return j 
print maxSubArraySum([-1, -1, 1, -1, 1, 0, 1, -1, -1])   
#print maxSubArraySum([1, 1, -1, -1, -1, -1, -1, 1, 1])

def Solution(S,P,Q):
    d={}
    d['A']=1
    d['C']=2
    d['G']=3
    d['T']=4
    j=len(P)
    l,n=[],[]
    for i in range(len(P)):
            n.append(sorted([d[x] for x in S[P[i]:Q[i]]+S[Q[i]]])[0]) 
    print str(n)          
        
Solution('CAGCCTA',[2,5,0],[4,5,6])  

def Solution(S,P,Q):
    d={}
    d['A']=1
    d['C']=2
    d['G']=3
    d['T']=4
    j=len(P)
    l,n,s=[],[],''
    for i in range(len(P)):
        s+=S[P[i]:Q[i]]+S[Q[i]]+":"
        #n.append(sorted([d[x] for x in S[P[i]:Q[i]]+S[Q[i]]])[0]) 
    print dict(s)    
    for i in s:
        if ":" in i:
            n.append(sorted(l)[0])
            l=[]
        else:    
            l.append(d[i])
            #print l
    return n   
        
        
Solution('CAGCCTA',[2,5,0],[4,5,6])   
   
def solution(A):
    h={}
    j=0
    for i in A:
        if i not in h.keys():
            h[i]=i
            j+=1
    return j
print solution([2,1,1,3,2,1])   

def solution(A):
    import itertools
    a=itertools.combinations(A,3)
    c=0
    if len(A) > 2:
        b1=set(sorted(list(a)))
        b=list(b1)
        for i in range(len(b)):
            P,Q,R=b[i][0],b[i][1],b[i][2]
            if 0 <= P and P + Q > R and R+Q > P:
                c=1
                break    
    return c    
print solution([10,2,5,1,8,20,1,2,3,4,5])  
print solution([10,50,5,1])  
print solution([-1,-1,-1])   
print solution([])

def solution(A):
    b,c=sorted(A),0
    for i in range(len(A)):
        if i < len(A)-2 and b[i]+b[i+1] > b[i+2]:
            c=1
            break
    return c 
print solution([10,2,5,1,8,20,1,2,3,4,5])  
print solution([10,50,5,1])  
print solution([-1,-1,-1])   
print solution([])      

from numpy import multiply
def solution(A):
    import itertools
    j,a=0,[]
    
    if len(A) == 3:
        j=A[0]*A[1]*A[2]
    b=set(itertools.combinations(A,3))
    for i in b:
        c=i[0]*i[1]*i[2]
        if j == 0 or j < c:
            j=c    
    j=j  
    return j
print solution([-5, -6, -4, -7, -10])

def solution(A):
    b=sorted(A)
    c=0
    j=0
    k=b[0]*b[1]*b[-1]
    for i in range(len(b)-2):
        c=b[i]*b[i+1]*b[i+2]
        if c > k or c==0:
            j=c
        else:
            j=k    
    return j
print solution([-5, 5, -5, 4,4])     

hash1={}
import re
list1=[]
file1=open("/Users/ashishsingh/para")
for i in file1:
    x=re.compile('(\,|\.|\')')
    print x.sub(" ",i)
    =
#subc=re.compile('(\,|\.|\')')
#subc=('(\,|\.|\')')
##file2=subc.sub(" ", str(file1))
##print file2
#for line in file2:
#        if len(line.lower()) > 1:
#               print line

def solution(S):

    for i in range(len(S)):
            S=S.replace('[]','')
            S=S.replace('()', '')
            S=S.replace('{}', '')
    if len(S) > 0:
        return 0
    else:
        return 1    
print solution("{[()()]}")  
print solution("([)()]")    

def solution(S,N):
    a=[]
    def element(Y,N):
        c=0
        T=1
        Z=Y.replace('<>', '')
        D=Z[:]
        for i in Z:
            print Z,N
            if i == '<' or i == '>' and T <= N:
                Z=Z.replace(i, '<>', 1)
                T+=1
                Z=Z.replace('<>', '', 1)            
        if len(Z) > 0:
            a.append(0)
        else:
            a.append(1)            
 
    for i,v in enumerate(S):
        element(v,N[i])
    return a    
print solution(['<>>>','<>>>>','<>','<>><'],[2,2,1,0])                
              
def solution(expressions,maxReplacements):
    a=[]
    def element(Y,N):
        Z=Y.replace('<>', '')
        for i in Z:
            print Z,N
            if i == '<' or i == '>' and N > 0:
                Z=Z.replace(i, '<>', 1)
                N-=1
                Z=Z.replace('<>', '', 1)            
        if len(Z) > 0:
            a.append(0)
        else:
            a.append(1)            
 
    for i,v in enumerate(expressions):
        element(v,maxReplacements[i])
    return a    
print solution(['<>>>','<>>>>'],[2,2])  

def solution(expressions,maxReplacements):
    new_return=[]
    def element(Y,N):
        Z=Y.replace('<>','')
        for i in Z:
            if (i == '<' or i == '>') and  N > 0:

                    Z=Z.replace(i, '<>', 1)
                    N-=1
                    Z=Z.replace('<>','')
                    print Z,N
        if len(Z) > 0:
            new_return.append(0)
        else:
            new_return.append(1)
    for k,v in enumerate(expressions):
        element(v,maxReplacements[k])
    return new_return  
print solution(['<>>>','<>>>>','<>>>>>><'],[2,2,5])      

class Shape(object):
    sides = 4

class Square(Shape):
    pass

class Triangle(Shape):
    pass

print (Shape.sides, Square.sides, Triangle.sides)
Triangle.sides = Triangle.sides - 1
print (Shape.sides, Square.sides, Triangle.sides)
Shape.sides = Square.sides + 2
print (Shape.sides, Square.sides, Triangle.sides)       

def solution(A,a=[]):
    sum1=0
    y=len(A)
    for k,i in enumerate(A):
        c=(y+k)-y
        sum1=sum(A[0:k+1])
        if sum1 > -1:
            a.append((c,sum1))    
    A.remove(A[0])
    if len(A) > 0:
        return solution(A)
    if len(a) > 0:
        return sorted(a, key=lambda x: x[0])[-1][0]+1
    else:
        return 0
print solution([-1,-1])           


def solution(A,a=[-1]):
    sum1=0 
    for k,i in enumerate(A):
        c=k
        sum1=sum(A[0:k+1])
        if sum1 > -1:
            if a[0] < c:
                a[0] = c       
    
    A.remove(A[0])
    if len(A) > 0:
        return solution(A)
        
    if a[0] >= 0:
        return a[0]+1
    else:
        return 0

print solution([-1,-1])

def solution(A,a=[-1]):
    sum1=0 
    for k,i in enumerate(A):
        c=k
        sum1=sum(A[0:k+1])
        if sum1 > -1:
            if a[0] < c:
                a[0] = c       
    
    A.remove(A[0])
    if len(A) > 0:
        return solution(A)
        
    if a[0] >= 0:
        return a[0]+1
    else:
        return 0

def solution(S):
    S=S.replace('()','')
    if '()' in S:
        return solution(S)
    if len(S) == 0:
        return 1
    else:
        return 0    

print solution(')(')
print solution('(((())))')
'''
def solution(S):
    b=[]
    for j,i in enumerate(S):
        if i == '(' or len(b) == 0:
            b.append(i)
           
        if i == ')' and b[-1] != ')':
            b.pop(-1)
            
  
    if len(b) > 0:
        return 0
    else:
        return 1
              
   
print solution(')(')
print solution('(((())))')  
print solution('') 
print solution('(()(())())') 
print solution('())')
print solution('((())') 