import stacks
st1=stacks.Lstack()
x=10
while st1.count<=stacks.Lstack.capacity:
		if st1.count==stacks.Lstack.capacity:
			raise Exception("Stack out of range")
		else:
		 	st1.push(x)
		 	x+=10