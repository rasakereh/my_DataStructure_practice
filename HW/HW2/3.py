def LG(n):
	'''ceil log'''
	a = 0
	while n != 0:
		a += 1
		n >>= 1
	
	a += (n > (1 << a))
	
	return a

'''class Stack:
	S = [0] * 10000
	sp = 0
	
	def push(self, value):
		S[self.sp] = value
		self.sp += 1
	
	def pop(self):
		self.sp -= 1
		return S[self.sp]
	
	def isEmpty(self):
		return self.sp == 0
'''
class Node:
	value = 0
	
	parent = None
	left = None
	right = None
	
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value

class Heap:
	H = [0] * 11000
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
		self.inorder = [0] * (1 << h)
		
		for a in range(1, h+1):
			for k in range(1 << (h-a)):
				#print("A[" + str((k << a) + (1 << (a-1))) + "] = " + str((1 << (h-a)) + k))
				self.inorder[(k << a) + (1 << (a-1))] = self.H[(1 << (h-a)) + k]
		i = 0
		for j in range(len(self.inorder)):
			if self.inorder[j] != 0:
				self.inorder[i] = self.inorder[j]
				i += 1
		
		self.inorder = self.inorder[:i]
		
	'''def inorderTraverse(self, index = 1):
		S = Stack()
		S.push(index)
		
		while not S.isEmpty():
			curIndex = S.pop()
			S.push(index << 1)
			
		self.inorderTraverse(index << 1)
		self.inorder += [self.H[index]]
		self.inorderTraverse((index << 1) + 1)'''
			

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

