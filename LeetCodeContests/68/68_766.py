matrix =[[1,2],[2,2]]
if any(matrix[i][j] != matrix[i+1][j+1] for i in range(len(matrix)-1) for j in range(len(matrix[0])- 1)):
    print(False)
else:
    print(True)

