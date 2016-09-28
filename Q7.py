n = int(input("enter N: "))

matrix = []

for i in range(n):
	r = [x for x in input().split(',')]
	matrix.append(r)


clockwise_rotate = [[row[i] for row in reversed(matrix)] for i in range(n)]
print(clockwise_rotate)


'''
input format:
4
1, 2, 3, 4
9, 8, 5, 6
6, 5, 3, 7
9, 2, 6, 8


​[1, 2, 3, 4]    [9, 6, 9, 1]

[9, 8, 5, 6] –> [2, 5, 8, 2]

[6, 5, 3, 7]    [6, 3, 5, 3]

[9, 2, 6, 8]    [8, 7, 6, 4]


'''
