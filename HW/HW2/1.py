class Heap:
	'''MIN HEAP'''

	__H = [0] * 600
	
	size = 0
	
	def insert(self, value):
		self.size = self.size + 1
		self.__H[self.size] = value
		self.__place(self.size)
		
	def min(self):
		return self.__H[1]
		
	def __place(self, index):
		pIndex = index // 2
		while pIndex > 0 and self.__H[index] < self.__H[pIndex]:
			self.__H[index], self.__H[pIndex] = self.__H[pIndex], self.__H[index]
			index = pIndex
			pIndex = index // 2
	
	
class Cell:
	content = '.'
	
	colAfter = 0
	rowAfter = 0
	
	maxRowExpand = 0
	maxColExpand = 0
	
n, m = list(map(int, input().split(" ")))

table = [[Cell() for i in range(m)] for j in range(n)]

for i in range(n):
	currentRow = input()
	for j in range(len(currentRow)):
		table[i][j].content = currentRow[j]
	
for row in table:
	colCount = 0
	for i in range(m-1, -1, -1):
		cell = row[i]
		if cell.content == '.':
			colCount = colCount + 1
		else:
			colCount = 0
		
		cell.colAfter = colCount

for j in range(m):
	rowCount = 0
	for i in range(n-1, -1, -1):
		cell = table[i][j]
		if cell.content == '.':
			rowCount = rowCount + 1
		else:
			rowCount = 0
		
		cell.rowAfter = rowCount

for row in table:
	H = Heap()
	for i in range(m-1, -1, -1):
		cell = row[i]
		if cell.content == '.':
			H.insert(cell.rowAfter)
		else:
			H = Heap()
		
		cell.maxColExpand = cell.colAfter * H.min()

for j in range(m):
	rowCount = 0
	for i in range(n-1, -1, -1):
		cell = table[i][j]
		if cell.content == '.':
			rowCount = rowCount + 1
		else:
			rowCount = 0
		
		cell.rowAfter = rowCount

for j in range(m):
	H = Heap()
	for i in range(n-1, -1, -1):
		cell = table[i][j]
		if cell.content == '.':
			H.insert(cell.colAfter)
		else:
			H = Heap()
		
		cell.maxRowExpand = cell.rowAfter * H.min()

maxSurface = 0

for row in table:
	for cell in row:
		maxExpansion = max(cell.maxColExpand, cell.maxRowExpand)
		if maxSurface < maxExpansion:
			maxSurface = maxExpansion

print(maxSurface)
