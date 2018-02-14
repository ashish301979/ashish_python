import os,sys,signal,time
def signal_handler(signum,frame):
	raise Exception("Time Out !!!!")
def ashish():
	print "ashish"
signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(5)   # Ten seconds
try:
    ashish()
    time.sleep(10)
except Exception, msg:
    print "Timed out!"
