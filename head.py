import sys
text = open(sys.argv[1],"r").readlines()
for i in range(0,5):
	print(str(text[i]))