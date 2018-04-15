'''
5
1 2 3 4 5
10 9 8 7 6
1 1 1 1 1
6 7 8 9 10
5 4 3 2 1
'''

matDim = int(input())
matrix = []
for _ in range(matDim):
    matrix.append([int(x) for x in input().split()])

distance_arr = [[0]*matDim for _ in range(matDim)]
max_arr      = [[0]*matDim for _ in range(matDim)]
min_arr      = [[0]*matDim for _ in range(matDim)]

for i in range(matDim):
    for j in range(matDim):
        if i == j == 0:
            max_arr[i][j] = matrix[i][j]
            min_arr[i][j] = matrix[i][j]
        if i == 0:
            max_arr[i][j] = max_arr[i][j-1] + matrix[i][j]
            min_arr[i][j] = min_arr[i][j-1] + matrix[i][j]
        elif j == 0:
            max_arr[i][j] = max_arr[i-1][j] + matrix[i][j]
            min_arr[i][j] = min_arr[i-1][j] + matrix[i][j]
        else:
            max_arr[i][j] = max(max_arr[i][j-1],max_arr[i-1][j]) + matrix[i][j]
            min_arr[i][j] = min(min_arr[i][j-1],min_arr[i-1][j]) + matrix[i][j]
print(max_arr[matDim-1][matDim-1], min_arr[matDim-1][matDim-1])

