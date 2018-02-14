#!/usr/bin/python
import multiprocessing
import collections,sys
words = [line.strip() for line in open("ashish_file.txt").readlines()]
print(len(words))
target='The Tribes and Castes of the Central Provinces of India'
chunksize=90000
def worker(i):
	try:
		return i + words[i:i+chunksize+1] .index(target)
	except ValueError:
		return None
pool=multiprocessing.Pool(processes=4)
results=pool.map(worker,range(0, len(words), chunksize))
pool.close()
a=[r for r in results if r is not None]
print len(a)
