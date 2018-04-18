class Heap:
	#Max Heap
	
	H = [0] * 100000
	size = 0
	
	def insert(self, value):
		self.size += 1
		self.H[self.size] = value
		index = self.size
		pIndex = index >> 2
		while pIndex > 0 and self.H[pIndex] < self.H[index]:
			self.H[pIndex], self.H[index] = self.H[index], self.H[pIndex]
			index = pIndex
			pIndex = index >> 2
	
	def pop(self):
		value = self.H[1]
		self.H[self.size], self.H[1] = self.H[1], self.H[self.size]
		size -= 1
		
		index = 1
		while True:
			lIndex = index << 1
			rIndex = lIndex + 1
			if lIndex > self.size:
				break
			if rIndex > self.size:
				maxIndex = lIndex
			else:
				if self.H[lIndex] > self.H[rIndex]:
					maxIndex = lIndex
				else:
					maxIndex = rIndex
			
			self.H[maxIndex], self.H[index] = self.H[index], self.H[maxIndex]
			index = maxIndex
		
		return value
	
	def empty(self):
		return self.size == 0
	

class Ostaad:
	hIndex = 0
	location = 0
	
	def __str__(self):
		return "Ostaad: " + str(self.hIndex) + " is at " + str(self.location)
	
	def __init__(self, hIndex = 0, location = 0):
		self.hIndex = hIndex
		self.location = location
	
	def __lt__(self, ostaadB):
		return self.hIndex < ostaadB.hIndex
	
	def __gt__(self, ostaadB):
		return self.hIndex > ostaadB.hIndex


def addIfPossible(index, p, pointers, hIndexes, H):
	if 


n = int(input()) - 1

locations = list(map(int, input().split()))
values = list(map(int, input().split()))
pointers = []
hIndexes = []

lastHIndex = float('Inf')

for i in range(n-1, -1, -1):
	if locations[i] == 1:
		if(lastHIndex > values[i]):
			lastHIndex = values[i]
			pointers += [i]
			hIndexes += [values[i]]

pointers += [-1]

N = len(pointers)

for i in range(N):
	p[i] = pointers[i]

for i in range(1, N):
	values[pointers[i]+1 : pointers[i-1]] = sorted(values[pointers[i]+1 : pointers[i-1]])


H = Heap()
	
for i in range(N):
	 addIfPossible(i, p, pointers, hIndexes, H)


print(values)
		
		
