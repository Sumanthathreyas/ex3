class Lstack:
	capacity = 10
	def __init__(self):
		self.count=0
		self.data=[]
	def isempty(self):
		return self.count==0
	def length(self):
		return self.count
	def isfull(self):
		return self.count==Lstack.capacity
	def peek(self):
		return self.data[-1]
	def push(self,key):
		'''if self.isfull():
			Lstack.capacity = 2*Lstack.capacity
			self.data.append(key)
			self.count+=1
		else:'''
		self.data.append(key)
		self.count+=1
	def pop(self):
		if not self.isempty():
			self.count-=1
			return self.data.pop()
