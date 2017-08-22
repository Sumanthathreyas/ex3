import sys
data=open(sys.argv[1]).readlines()
data=list(map(int,data))
print(sum(data))