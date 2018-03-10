H = [0] * 100
n = 1

def insert(elem):
	global n
	
	H[n] = elem
	index = n
	while index > 1 and H[index] > H[index//2]:
		H[index], H[index//2] = H[index//2], H[index]
		index //= 2
	
	n += 1
	
def heapify(i):
	maxIndex=0
	
	while(2*i+1 < n):
		if H[2*i] > H[2*i+1]:
			maxIndex=2*i
		else:
			maxIndex=2*i+1

		if H[i] > H[maxIndex]:
			maxIndex=i
	
		if maxIndex != i:
			H[i], H[maxIndex] = H[maxIndex], H[i]
			i = maxIndex
		else:
			break

def pop():
	global n
	n -= 1
	H[1], H[n] = H[n], H[1]
	heapify(1)
	return H[n]
	
def heapsort(A):
	res = []
	for i in A:
		insert(i)
	
	while n != 1:
		elem = pop()
		res += [elem]
		
	return res

A = [1, 3, 4, 1, 1, 5, 6, 2, 6, 2, 7, 1, 4, 9]

X = heapsort(A)

print(A)
print(X)

