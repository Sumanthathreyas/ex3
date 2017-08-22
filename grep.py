import sys
data=open(sys.argv[2]).readlines()
for i in range(len(data)):
	if sys.argv[1] in data[i]:
		print(data[i])