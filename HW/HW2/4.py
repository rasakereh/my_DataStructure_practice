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

class Heap:
	H = [Ostaad()] * 110000
	size = 0
		
	def insert(self, value):
		self.size += 1
		self.H[self.size] = value
		index = self.size
		pIndex = index >> 1
		while pIndex != 0 and self.H[index] < self.H[pIndex]:
			self.H[index], self.H[pIndex] = self.H[pIndex], self.H[index]
			index = pIndex
			pIndex = index >> 1
	
	def pop(self):
		value = self.H[1]
		self.H[self.size], self.H[1] = self.H[1], self.H[self.size]
		
		index = 1
		self.size -= 1
		
		while True:
			minIndex = 1
			lIndex = index << 1
			rIndex = (index << 1) + 1
			if lIndex > self.size:
				break
			if rIndex > self.size:
				minIndex = lIndex
			else:
				if self.H[rIndex] < self.H[lIndex]:
					minIndex = rIndex
				else:
					minIndex = lIndex
			if self.H[minIndex] < self.H[index]:
				self.H[index], self.H[minIndex] = self.H[minIndex], self.H[index]
				index = minIndex
			else:
				break
		
		return value
		
	def isEmpty(self):
		return self.size == 0


n = int(input()) - 1

h = Heap()

locations = list(map(int, input().split()))
values = list(map(int, input().split()))

for i in range(n):
	if locations[i] == 1:
		h.insert(Ostaad(values[i], i))


begin = 0
end = -1

unitCnt = 0

while not h.isEmpty():
	ezOstaad = h.pop()
	courseLimit = ezOstaad.hIndex - 1
	end = ezOstaad.location
	
	if end - begin < courseLimit:
		unitCnt += sum(values[begin:end])
	else:
		unitCnt += sum(sorted(values[begin:end], reverse = True)[0:courseLimit])
	
	begin = ezOstaad.location + 1

print(unitCnt)


