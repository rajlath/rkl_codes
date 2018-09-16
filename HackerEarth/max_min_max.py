x =1
matrix=[]
for i in range(3):
    tm = []
    for j in range(3):
        tm.append(x)
        x += 1
    matrix.append(tm)
col_mat = list(zip(*matrix))
print(matrix)
print(col_mat)