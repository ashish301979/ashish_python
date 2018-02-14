#!/usr/bin/python
import sys
sticker=sys.argv[1]
name=sys.argv[2]
sticker_count=1
sticker_org=sys.argv[1]
for l in name:
	if l in sticker:
		sticker=sticker.replace(l, "", 1)	
        		
	else:
		sticker_count+=1
		sticker=sticker+sticker_org
print(sticker_count)
