import stacks
import queues
import sys
s=stacks.Lstack()
q=queues.FlexiQueue()
y=int(sys.argv[1])
value=10
for i in range(5):
	s.push(value)
	value+=10
print(s.data)
def search(x):
	count = 0
	for i in range(s.length()):
		ele = s.pop()
		q.enque(ele)
		if ele == x:
			count = 1
	for i in range(q.length()):
		ele = q.deque()
		s.push(ele)
	for i in range(s.length()):
		ele = s.pop()
		q.enque(ele)
	for i in range(q.length()):
		ele = q.deque()
		s.push(ele)
	print(s.data)
	return count
count = search(y)
if count == 1:
	print("Element is Found in Stack")
else:
	print("Element is not found in Stack")

