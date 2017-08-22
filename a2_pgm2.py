import stacks
s=stacks.Lstack()
l1=[1,2,3,4,5]
for i in range(0,len(l1)):
	s.push(l1[i])
print "Input ",s.data
l2=[]
while(not s.isempty()):
	l2.append(s.pop())
print "output ",l2



