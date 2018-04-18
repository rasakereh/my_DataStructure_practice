def LG(n):
	'''ceil log'''
	a = 0
	while n != 0:
		a += 1
		n >>= 1
	
	a += (n > (1 << a))
	
	return a

class Node:
	value = 0
	
	parent = None
	left = None
	right = None
	
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value

class Heap:
	H = [0] * 15000
	size = 0
	
	inorder = []
	
	def insert(self, value):
		self.size += 1
		self.H[self.size] = value
		index = self.size
		pIndex = index >> 1
		while pIndex != 0 and self.H[index] < self.H[pIndex]:
			self.H[index], self.H[pIndex] = self.H[pIndex], self.H[index]
			index = pIndex
			pIndex = index >> 1
	
	def inorderTraverse(self):
		h = LG(self.size+1)		#height of Heap
		n = 1 << h
		self.inorder = [0] * n
		
		for a in range(1, h+1):
			for k in range(1 << (h-a)):
				self.inorder[min(n-1, (k << a) + (1 << (a-1)))] = self.H[min(11000, (1 << (h-a)) + k)]
		
		i = 0
		for j in range(n):
			if self.inorder[j] != 0:
				self.inorder[i] = self.inorder[j]
				i += 1

n = int(input())

bst = [0] * n

h = Heap()

for i in range(n):
	k = int(input())
	bst[i] = k
	h.insert(k)

bst = sorted(bst)

h.inorderTraverse()

cnt = 0

for i in range(n):
	cnt += (bst[i] != h.inorder[i])
	
print(cnt)

