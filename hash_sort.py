''''h={}
fh=open("abc")
for i in fh:
    if i.split()[0] not in h.keys():
        v=[]
        key=i.split()[0]
        v.append(i.strip().split(" ", 1)[1])
    else:
        v.append(i.strip().split(" ", 1)[1])
    h[key]=v
for k,v in h.items():
    print k," ".join(v)
    print type("".join(v))
    
print sorted(h.items(), key=lambda x: x[1])   

 '''       