def binarySearch(A, x):
'''
@param A array(sorted)
The function tries to find and return pair of (i, j) in a way that:
	A[i], A[i+1], ... A[j] = x
Array that is not sorted may cause undefined behavior.
'''
	start = 0
	end = len(A) - 1
	
	found = -1
	lfound = -1
	rfound = -1
	
	count = 0
	
	while count == 0 or found != -1:
		count += 1
		if found != -1:
			end = found - 1
			found = -1
		
		while end >= start:
			middle = (end + start) // 2
			if A[middle] < x:
				start = middle + 1
			elif A[middle] > x:
				end = middle - 1
			else:
				found = middle
				lfound = found
				break
				
	start = 0
	end = len(A) - 1
	found = -1	
	count = 0
	
	while count == 0 or found != -1:
		count += 1
		if found != -1:
			start = found + 1
			found = -1
		
		while end >= start:
			middle = (end + start) // 2
			if A[middle] < x:
				start = middle + 1
			elif A[middle] > x:
				end = middle - 1
			else:
				found = middle
				rfound = found
				break
	
	return lfound, rfound
	
	
	
	
A = [1, 2, 2, 3, 4, 7, 9, 10, 12, 13, 15, 16, 16, 16]

print(binarySearch(A, 16))
print(binarySearch(A, 2))
print(binarySearch(A, 9))
print(binarySearch(A, 6))

