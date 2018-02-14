# -*- coding: utf-8 -*-
import sys,re
import datetime,time
a=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
result=[]
print """Question 1 : In which one of the following page replacement policies, Belady’s anomaly may occur?
	(A) FIFO (B) Optimal(C) LRU (D) MRU"""
ans=raw_input("Please Select the Correct Option from The above : ")
if ans.lower().strip() == "a".strip():
		result.append("T")
else:
		result.append("F")
print "Your Answers is Saved : "
b=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
print "Time Remaining for this test : ",30-(b-a),"Minutes"

print """Question 2 : Consider a main memory with five page frames and the following sequence of page references: 3, 8, 2, 3, 9, 1, 6, 3, 8, 9, 3, 6, 2, 1, 3. Which one of the following is true with respect to page replacement policies First In First Out(FIFO) and Least Recently Used(LRU)?

	(A) Both incur the same number of page faults.(B) FIFO incurs 2 more page faults than LRU(C) LRU incurs 2 more page faults than FIFO(D) FIFO incurs 1 more page faults than LRU. """
print
ans=raw_input("Please Select the Correct Option from The above : ")
if ans.lower().strip() == "a".strip():
        	result.append("T")
else:
        	result.append("F")
print "Your Answers is Saved : "
b=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
print "Time Remaining for this test : ",30-(b-a),"Minutes"
print
print """Question 3 : A process refers to  5 pages, A,  B, C,  D and E in the following order A,  B,  C,  D,  A,  B,  E,  A,  B,  C,  D,  E. If the page replacement algorithm is FIFO, the number of page transfer with an empty internal store of 3frames is: 

	A) 8   B)  10   C)  9	D)  7"""
print
ans=raw_input("Please Select the Correct Option from The above : ")
if ans.lower().strip() == "c".strip():
        	result.append("T")	
else:
        	result.append("F")

print "Your Answers is Saved : "
b=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
print "Time Remaining for this test : ",30-(b-a),"Minutes"
print
print """Question 4 : A system has 3 processes sharing 4 resources. If each process needs a maximum of 2 units then :
 
A)  deadlock can never occur			B)   deadlock may occur         C)  deadlock has to occur     			D)  None of the above"""
print
ans=raw_input("Please Select the Correct Option from The above : ")
if ans.lower().strip() == "a".strip():
        	result.append("T")
else:
        	result.append("F")
print "Your have answered all the question : "
print result
