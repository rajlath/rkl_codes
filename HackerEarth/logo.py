'''
6 6
......
.1111.
.1..1.
.1..1.
.1111.
......
'''

n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])
for i in range(n):
    one_count = str(matrix[i]).count("1")
    if one_count == 0:continue




