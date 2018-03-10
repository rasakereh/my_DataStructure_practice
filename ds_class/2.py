def count_sort(arr):
	MIN = min(arr)
	MAX = max(arr)
	
	result = [0 for i in range(MAX - MIN + 1)]
	
	for i in arr:
		result[i - MIN] += 1
	
	strRes = ""
	for i in range(len(result)):
		for j in range(result[i]):
			strRes += str(i + MIN) + " "
			
	return strRes
	

arr = [1, 2, 2, 2, 1, 3, 4, 1, 7, 1, 9, 0, 2, 4, 1]

print(count_sort(arr))

