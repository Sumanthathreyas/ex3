import queues
q = queues.FlexiQueue()
def push(key):
	q.enque(key)
def pop():
	ele = q.data[q.size-1]
	q.data[q.size-1] = None
	q.size-=1
	return ele
def length():
	return q.length()
def peek():
	ele = q.data[q.size-1]
	return ele
