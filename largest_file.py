import os
import sys

files=[i for i in os.listdir(sys.argv[1]) if os.path.isfile(i)]

max_size = 0
file_name = None

for i in files:
	size = os.path.getsize(i)
	if size>max_size:
		max_size=size
		file_name = i

print 'The largest file : ',file_name,' has : ',max_size,' bytes'
