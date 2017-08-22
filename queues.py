class FlexiQueue:
	capacity = 2
	def __init__(self):
		self.data=[None]*FlexiQueue.capacity
		self.size=0
		self.front=0
	def isempty(self):
		return self.size == 0
	def isfull(self):
		return self.size == len(self.data)
	def first(self):
		return self.data[self.front]
	def length(self):
		return self.size
	def enque(self,key):
		if self.isfull():
			self.resize(2*len(self.data))
		next = (self.front+self.size)%(len(self.data))
		self.data[next] = key
		self.size+=1
	def deque(self):
		if not self.isempty():
			ele = self.data[self.front]
			self.data[self.front] = None
			self.front=(self.front+1)%(len(self.data))
			self.size-=1
		if 0 < self.size < len(self.data)//4:
			self.resize(len(self.data)//2)
		return ele
	def resize(self,capacity):
		old = self.data
		walk = self.front
		self.data= [None]*capacity
		for k in range(self.size):
			self.data[k]=old[walk]
			walk=(walk+1)%len(old)
		self.front=0
