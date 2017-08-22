import sys
def lc(flr):
	print(len(open(flr,"r").readlines()))
lc(sys.argv[1])
def cc(flr):
	print(len(open(flr,"r").read()))
cc(sys.argv[1])
def wc(flr):
	print(len(open(flr,"r").read().split()))
wc(sys.argv[1])