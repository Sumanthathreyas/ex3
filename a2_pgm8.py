import stacks
import a2_pgm1
s=stacks.Lstack()
t=stacks.Lstack()
def enque(key):
	if not s.isfull():
		s.push(key)
def deque():
	if not s.isempty():
		a2_pgm1.transfer(s,t)
		ele = t.pop()
		a2_pgm1.transfer(t,s)
		return ele
def length():
	return s.length()
def front():
		a2_pgm1.transfer(s,t)
		ele = t.peek()
		a2_pgm1.transfer(t,s)
		return ele