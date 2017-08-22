import os,time
import sys
size = sys.argv[2]
if size[-1] == 'k':
	print(int(size[:-1]))
	size = int(size[:-1])*1024
elif size[-1] == 'm':
	size = int(size[:-1])*1024*1024
elif size[-1] == 'g':
	size = int(size[:-1])*1024*1024*1024
elif size[-1] == 'b':
	size = int(size[:-1])
else:
	print("Invalid Size")
	exit()
files=[i for i in os.listdir(sys.argv[1]) if os.path.isfile(i)]
file_large = []
for f in files:
	if os.path.getsize(f) > size:
		file_large.append(f)
print(file_large)