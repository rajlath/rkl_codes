n = int(input())
matrix = []
for i in range(n):
    matrix.append([x for x in input()])

count = 0

for i in range(n):
    for j in range(n):
        if (j+1) < n and (i + 1) < n and (j-1)> -1 and (i-1) > -1:
            count += (matrix[i][j] == matrix[i-1][j-1] == matrix[i-1][j+1] == matrix[i+1][j-1] == matrix[i+1][j+1] ==  "X")
print(count)
