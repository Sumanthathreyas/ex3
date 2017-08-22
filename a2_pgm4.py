import stacks
s=stacks.Lstack()
t=stacks.Lstack()
u=stacks.Lstack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("s is : ",s.data)
def transfer(s,t):
	while(not s.isempty()):
		t.push(s.pop())
transfer(s,t)
transfer(t,u)
transfer(u,s)
print("After reverse s is : ",s.data)