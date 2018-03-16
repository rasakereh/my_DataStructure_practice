def selectionSort(A):
	result = [0] * len(A)
	for i in range(len(A)):
		minI = i
		for j in range(i+1, len(A)):
			if A[j] < A[minI]:
				minI = j
		A[i], A[minI] = A[minI], A[i]
		result[i] = A[i]
	
	return result

def merge(A, B):
	aI = 0
	bI = 0
	aN = len(A)
	bN = len(B)
	N = aN + bN
	
	result = [0] * N
	
	for i in range(N):
		if aI == aN:
			result[i] = B[bI]
			bI += 1
		elif bI == bN:
			result[i] = A[aI]
			aI += 1
		elif A[aI] <= B[bI]:
			result[i] = A[aI]
			aI += 1
		else:
			result[i] = B[bI]
			bI += 1
	
	return result

def mergesort(A):
	if len(A) <= 5:
		return selectionSort(A)
	middle = len(A)//2
	
	X = mergesort(A[:middle])
	Y = mergesort(A[middle:])
		
	return merge(X, Y)

n = int(input())

A = [0] * n
B = [0] * n

for i in range(n):
	A[i], B[i] = list(map(int, input().split(" ")))

A = mergesort(A)
B = mergesort(B)

currentOpenCount = 0
maxOpenCount = 0

aI = 0
bI = 0

aN = len(A)
bN = len(B)

N = aN + bN

for i in range(N):
	if aI == aN:
		currentOpenCount -= 1
		bI += 1
	elif A[aI] <= B[bI]:
		currentOpenCount += 1
		aI += 1
		if currentOpenCount > maxOpenCount:
			maxOpenCount = currentOpenCount
	else:
		currentOpenCount -= 1
		bI += 1
		
print(maxOpenCount)

