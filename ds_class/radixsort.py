def BSort(A, digit):
	res = [[] for i in range(10)]
	for i in A:
		dig = (i // (10 ** digit)) % 10
		res[dig] += [i]
	
	i = 0
	for bucks in res:
		for nums in bucks:
			A[i] = nums
			i += 1
	
def RadixSort(A, maxLen):
	for i in range(maxLen):
		BSort(A, i)
	
A = [123, 421, 23, 441, 5, 1, 111, 5, 532, 7, 542, 135, 731, 913, 915, 835, 14, 732, 145]

RadixSort(A, 3)

print(A)
