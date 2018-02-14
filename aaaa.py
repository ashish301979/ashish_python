import itertools

def slicefile(filename, start, end):
    lines = open(filename)
    return itertools.islice(lines, start, end)

out = open("blah.txt", "a+")
j=0
k=0
for i in range(100):
	for line in slicefile("ashish_file.txt", j, k):
		j=k
		k=j+30
    		out.write(line)
