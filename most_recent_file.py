import os,time
import sys

files=[i for i in os.listdir(sys.argv[1]) if os.path.isfile(i)]

file_name = max(files, key = os.path.getmtime)
reform = time.ctime(os.path.getmtime(file_name))

print 'The file : ',file_name,' has changed on : ',reform

