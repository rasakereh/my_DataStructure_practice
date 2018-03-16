def insertionSort(A):
	n = len(A)
	for i in range(n-1):
		j = i+1
		val = A[j]
		while j > 0 and val < A[j-1]:
			A[j] = A[j-1]
			j -= 1
		A[j] = val


def smallMedian(A):
	insertionSort(A)
	index = 0
	elem = 0
	if len(A) % 2 == 1:
		index = len(A)//2
		elem = A[index]
	else:
		#return (A[len(A)//2] + A[len(A)//2 - 1]) / 2.0
		index = len(A)//2
		elem = A[index]
	
	return index

def approxMedian(A, size = -1, portion = 5):
	if size == -1:
		size = len(A)
		
	if size <= portion:
		return smallMedian(A[0:size])
	
	k = 0
	
	for i in range(0, size, portion):
		index = i + smallMedian(A[i:min(i+portion, size)])
		A[k], A[index] = A[index], A[k]
		k += 1
	
	return approxMedian(A, k, portion)

def partition(A, medIndex):
	m = A[medIndex]
	A[0], A[medIndex] = A[medIndex], A[0]
	leftP = 1
	rightP = len(A) - 1
	
	while leftP < rightP:
		if A[leftP] <= m:
			leftP += 1
		elif A[rightP] >= m:
			rightP -= 1
		else:
			A[leftP], A[rightP] = A[rightP], A[leftP]
	
	if leftP == len(A) or A[leftP] > m:
		leftP -= 1
	A[0], A[leftP] = A[leftP], A[0]
	
	return leftP
	
def findElementK(A, k):
	approx_median = approxMedian(A)
	index = partition(A, approx_median)
	if index == k:
		return A[index]
	elif index > k:
		return findElementK(A[0:index], k)
	else:
		return findElementK(A[index+1:], k - index - 1)

def findIndex(A, elem):
	for i in range(len(A)):
		if A[i] == elem:
			return i
	
	return -1

#A = [30, 15, 20, 19, 5, 7, 2, 1, 25, 3, 29, 18, 14, 4, 27, 16, 6, 9, 24, 8, 12, 10, 21, 26, 13, 17, 22, 23, 28, 11]
#A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#A = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

n = int(input())

A = list(map(int, input().split(" ")))
median = findElementK(A, n//2)
index = findIndex(A, median)

partition(A, index)

A_strange = [0] * len(A)

k = 0

for i in range(1, n, 2):
	A_strange[i] = A[k]
	k += 1

for i in range(0, n, 2):
	A_strange[i] = A[k]
	k += 1

for i in A_strange:
	print(i, end = " ")

