#Quick Sort :D

def quicksort(arr, start, end):
	if start >= end:
		return
	needle = arr[start]
	place = start
	
	lesserP = start+1
	greaterP = end
	
	while lesserP < greaterP:
		if (arr[lesserP] > needle and arr[greaterP] < needle):
			arr[lesserP], arr[greaterP] = arr[greaterP], arr[lesserP]
		elif arr[lesserP] <= needle:
			lesserP += 1
		elif arr[greaterP] >= needle:
			greaterP -= 1
	
	if arr[lesserP] > needle:
		lesserP -= 1
	
	arr[lesserP], arr[place] = arr[place], arr[lesserP]
	place = lesserP
	
	quicksort(arr, start, place - 1)
	quicksort(arr, place + 1, end)
	
	
	
array = [7, 4, 4, 2, 4, 8, 9, 3, 1]
quicksort(array, 0, len(array)-1)
print(array)

