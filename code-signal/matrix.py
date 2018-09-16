matrix = [
[11, 21, 31, 41, 51, 61, 71],
[12, 22, 32, 42, 52, 62, 72],
[13, 23, 33, 43, 53, 63, 73],
[14, 24, 34, 44, 54, 64, 74],
[15, 25, 35, 45, 55, 65, 75],
[16, 26, 36, 46, 56, 66, 76],
[17, 27, 37, 47, 57, 67, 77] ]

rows = len(matrix)
cols = len(matrix[0])

def is_valid(matrix, i, j):
    return  0 <= i <= len(matrix) - 1 and 0 <= j <= len(matrix[0]) - 1

for i in range(rows):
    for j in range(cols):
        for x in [[0,1],[0,-1],[1,0], [-1,0]]:
            x1, v1 = i + x[0], j + x[1]
            if is_valid(matrix,x1,v1):
                print(matrix[x1][v1])


