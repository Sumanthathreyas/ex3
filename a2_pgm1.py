import stacks
s=stacks.Lstack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
#print("s is : ",s.data)
t=stacks.Lstack()
def transfer(s,t):
	while(not s.isempty()):
		t.push(s.pop())
transfer(s,t)
#print("t is : ",t.data)
