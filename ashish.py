import datetime,time
a=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
print a 
time.sleep(72)
b=datetime.datetime.now().hour*60+datetime.datetime.now().minute+datetime.datetime.now().second/60
time_new=b-a
print time_new
