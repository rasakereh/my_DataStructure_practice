def merge(a, b):
	res = []
	a_i = 0
	b_i = 0
	_a_ = len(a)
	_b_ = len(b)
	
	for i in range(_a_ + _b_):
		if a_i == _a_:
			res.append(b[b_i])
			b_i += 1
			continue
		if b_i == _b_:
			res.append(a[a_i])
			a_i += 1
			continue
		if a[a_i] <= b[b_i]:
			res.append(a[a_i])
			a_i += 1
		else:
			res.append(b[b_i])
			b_i += 1
	
	return res

def sort(a, start = 0, end = -1):
	if end == -1:
		end = len(a)-1
	if start > end:
		return []
	if start == end:
		return [a[start]]
	if end - start == 1:
		return [min(a[start], a[end]), max(a[start], a[end])]
	A = sort(a, start, (start+end) // 2)
	B = sort(a, (start+end) // 2 + 1, end)
	return merge(A, B)

a = [1, 4, 3, 2, 6, 3, 3, 5, 8, -2, 0, 3, 5, 10, 12, 3, 4]

print(a)
print(sort(a))

