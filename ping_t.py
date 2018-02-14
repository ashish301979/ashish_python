import os
a="localhost"
print os.popen("ping -c 2 " + a).readlines()
	
