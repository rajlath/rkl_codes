'''
Sample Input 0
n  m k
5 10 7
Sample Output 0

10 9 8 7 6
9 17 16 15 14
8 16 24 23 22
7 15 23 31 30
6 14 22 30 38
'''

n, m , k = [int(x) for x  in input().split()]
matrix = [[0 for x in range(n)]  for y in range(n)]
for i in range(n):
    for j in range(n):
        if i == j == 0: matrix[i][j] = m
        elif i == j: matrix[i][j] = matrix[i-1][j-1] + k
        elif i >  j: matrix[i][j] = matrix[i-1][j] - 1
        elif i <  j: matrix[i][j] = matrix[i][j-1] - 1
for i in matrix:
    print(" ".join(map(str, i)))        
