'''A double-ended queue (dequeue, often abbreviated to deque) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail).'''

import stacks
import a2_pgm1
s=stacks.Lstack()
t=stacks.Lstack()
def enqueAtFront(key):
	if not s.isfull():
		a2_pgm1.transfer(s,t)
		t.push(key)
		a2_pgm1.transfer(t,s)
def enqueAtRear(key):
	if not s.isfull():
		s.push(key)
def dequeAtFront():
	if not s.isempty():
		a2_pgm1.transfer(s,t)
		ele = t.pop()
		a2_pgm1.transfer(t,s)
		return ele
def dequeAtRear():
	if not s.isempty():
		ele = s.pop()
		return ele
def length():
	return s.length()
def frontElement():
		a2_pgm1.transfer(s,t)
		ele = t.peek()
		a2_pgm1.transfer(t,s)
		return ele
def rearElement():
		ele = s.peek()
		return ele