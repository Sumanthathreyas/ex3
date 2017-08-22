''' R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = 

[6, 7, 8,  9, 4, 5]'''

import stacks
r=stacks.Lstack()
s=stacks.Lstack()
t=stacks.Lstack()
r.push(1)
r.push(2)
r.push(3)
s.push(4)
s.push(5)
t.push(6)
t.push(7)
t.push(8)
t.push(9)
t_len=t.length()
print("R = ",r.data,"  ;  S = ",s.data,"  ; T = ",t.data)
def transfer(s,t):
	while(not s.isempty()):
		t.push(s.pop())
def transferLen(s,t,leng):
	while(leng!=0):
		t.push(s.pop())
		leng-=1
transfer(t,r)
transfer(s,t)
transferLen(r,s,t_len)
transfer(t,s)
print("R = ",r.data,"  ;  S = ",s.data,"  ; T = ",t.data)



