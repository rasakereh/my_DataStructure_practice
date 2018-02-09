#! /usr/bin/env python3

table = []

def unique_true(arr):
	result = -1
	for i in range(len(arr)):
		if arr[i]:
			if result != -1:
				return -1
			else:
				result = i
	
	return result
	

def make_table(table):
	for i in range(9):
		for j in range(9):
			if table[i][j][0] != 0:
				table[i][j][1:] = [0 for i in range(9)]
				continue
			for k in range(1,10):
				if k in [cols[0] for cols in table[i]]:
					table[i][j][k] = 0
				if k in [rows[j][0] for rows in table]:
					table[i][j][k] = 0
				if k in [table[a][b][0] for a in range(3*int(i/3), 3*int(i/3)+3) for b in range(3*int(j/3), 3*int(j/3)+3)]:
					table[i][j][k] = 0

def put_restricted(table):
	#first we handle cells with one possibility:
	for i in range(9):
		for j in range(9):
			possibility = unique_true(table[i][j][1:])
			if possibility != -1:
				table[i][j][0] = possibility + 1
				return [i, j]
	
	#then we may think of rows with one possible values:
	for i in range(9):
		for num in range(1, 10):
			possibility = unique_true([cols[num] for cols in table[i]])
			if possibility != -1:
				table[i][possibility][0] = num
				return [i, possibility]
	
	#now it is cols' turn:
	for j in range(9):
		for num in range(1, 10):
			possibility = unique_true([table[rows][j][num] for rows in range(9)])
			if possibility != -1:
				table[possibility][j][0] = num
				return [possibility, j]
	
	#the last case is a num with one possible place within a square:
	for square in range(9):
		sqX1 = (square % 3) * 3
		sqX2 = sqX1 + 3
		sqY1 = int(square/3) * 3
		sqY2 = sqY1 + 3
		for num in range(1, 10):
			possibility = unique_true([table[a][b][num] for a in range(sqX1, sqX2) for b in range(sqY1, sqY2)])
			if possibility != -1:
				i = int(possibility/3)
				j = possibility % 3
				table[i][j][0] = num
				return [i, j]
	
	return [-1,-1]

def upgrade(table, row, col):
	if row < 0 or col < 0:
		return 
		
	table[row][col][1:] = [0 for i in range(9)]
	
	num = table[row][col][0]
	
	for i in range(9):
		table[i][col][num] = 0
	
	for j in range(9):
		table[row][j][num] = 0
	
	sqX1 = int(row/3)*3
	sqX2 = sqX1 + 3
	sqY1 = int(col/3)*3
	sqY2 = sqY1 + 3
	
	for a in range(sqX1, sqX2):
		for b in range(sqY1, sqY2):
			table[a][b][num] = 0

def print_table(table):
	for row in table:
		this_row = ""
		for col in row:
			this_row += str(col[0]) + ","
		print(this_row)

def print_full_table(table):
	for i in range(9):
		for j in range(9):
			if table[i][j][0] == 0:
				this_row = "({0:d}, {1:d}): ".format(i, j)
				for num in range(1, 10):
					if table[i][j][num]:
						this_row += "{0:d} ".format(num)
				print(this_row)

for i in range(9):
	table.append(list(map(int, input().split(','))))

for i in range(9):
	for j in range(9):
		table[i][j] = [table[i][j]] + [1 for i in range(9)]

make_table(table)

while True:
	[row, col] = put_restricted(table)
	upgrade(table, row, col)
	input()
	print_table(table)

'''
	What I have learned:
	extracting a col of an array can be done by:   [row[col] for row in array]
	function calls for arrays are by reference.
	map function is good :))
	map is not subscriptable
	pdb debbuger
	python is much easier than C :)
'''

