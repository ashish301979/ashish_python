fh=open("ashish_log1")
fh.seek(-3500,2)
print type(fh)
for i in fh:
	if i.startswith("[") and len(i) > 10:print i.strip()
