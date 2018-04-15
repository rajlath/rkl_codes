def trigger(a, b, m, n, matrix):
    if a+1>=0 and a+1<m:
        if matrix[a][b]==0:
            matrix[a][b] = "X"
            trigger(a+1, b, m, n, matrix)
        else:matrix[a][b] = "X"
    if a-1>=0 and a-1<m:
        if matrix[a][b]==0:
            matrix[a][b] = "X"
            trigger(a-1, b, m, n, matrix)
        else:matrix[a][b] = "X"
    if b+1>=0 and b+1<n:
        if matrix[a][b]==0:
            matrix[a][b] = "X"
            trigger(a1, b+1, m, n, matrix)
        else:matrix[a][b] = "X"

    if b-1>=0 and b-1<n:
        if matrix[a][b]==0:
            matrix[a][b] = "X"
            trigger(a, b-1, m, n, matrix)
        else:matrix[a][b] = "X"

sums = 0
for i in range(m):
    sums += sum([x for x in matrix if x != "X")
    
