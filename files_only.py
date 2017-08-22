import os,time
import sys

files=[i for i in os.listdir(sys.argv[1]) if os.path.isfile(i)]
print(files)