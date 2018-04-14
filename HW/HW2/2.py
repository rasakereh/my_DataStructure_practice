class Node:
	value = 0
	height = 0
	cost = 0
	
	parent = None
	left = None
	right = None
	
	def __init__(self, parent, value, height):
		self.parent = parent
		self.value = value
		self.height = height
		self.cost = height
	
class BST:
	root = None
	
	def insert(self, value):
		if self.root == None:
			self.root = Node(None, value, 1)
			return True, self.root
		
		n = self.root
		
		inserted = True
		
		while True:
			if value > n.value:
				if n.right == None:
					n.right = Node(n, value, n.height+1)
					n = n.right
					break
				n = n.right
			elif value < n.value:
				if n.left == None:
					n.left = Node(n, value, n.height+1)
					n = n.left
					break
				n = n.left
			else:
				inserted = False
				break
		
		if inserted:
			self.updateCosts(n)
		
		return inserted, n
		
	def updateCosts(self, node):
		height = node.height
		while(node.parent != None):
			node.parent.cost = node.parent.cost + height
			node = node.parent
		

bst = BST()

n = int(input())

for i in range(n):
	inserted, node = bst.insert(int(input()))
	if not inserted:
		print(node.cost)


