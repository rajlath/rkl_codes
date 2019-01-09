nb_test = int(input())
for _ in range(nb_test):
    n = int(input())
    mat = [[0 for i in range(n)] for j in range(n)]
    begin = 1
    for i in range(1,n+1):
        for j in range(i):
            mat[j][i-1-j] = begin
            begin+=1
            print(mat)

    for i in range(n-1,0,-1):
        for j in range(i):
            mat[n-i+j][n-1-j]= begin
            begin+=1
    for i in range(n):
        print(*mat[i])