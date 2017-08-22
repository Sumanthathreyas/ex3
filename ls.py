from os import listdir
import sys
from os.path import isfile, join
if len(sys.argv)==2:
	print(listdir(sys.argv[1]))
elif len(sys.argv)==1:
	print(listdir('./'))
else:
	print("Error: More than 1 argument")
