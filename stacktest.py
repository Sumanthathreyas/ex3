import stacks

def test_emptystack():
	stk = stacks.LimitedStack()
	assert(stk.isempty())
	assert(stk.length == 0)

def test_normalstack():
	stk = stacks.LimitedStack()
	stk.push(10)
	stk.push(20.3)
	stk.push("hello")
	ele = stk.peek()
	print ele
	stk.display()

if __name__ == '__main__':
	#test_emptystack()
	test_normalstack()
