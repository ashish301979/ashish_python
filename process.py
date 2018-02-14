import subprocess,time
p1=subprocess.Popen(['python','process1.py'])
p2=subprocess.Popen(['python','process2.py'])
p1.wait()
p2.wait()
