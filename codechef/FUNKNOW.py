A = [[0] * 6 for _ in range(501)]
nots = int(input())
for _ in range(nots):
    nel = int(input())
    arr = [int(x) for x in input().split()]
    B   = [int(x) for x in input().split()]
    k = 1
    for i in range(1, 6):
        for j in range(1, nel+1):
            A[i][j] = A[i-1][j-1] + B[5-i]*k*arr[j-1]
            if j>i and A[i][j] < A[i][j-1]:
                A[i][j]=A[i][j-1]
        k = k * -1
    print(A[5][nel])

#!RUNTIME ERROR
