"""
First Line = noOfRows noOfCols
Next n lines =
Matrix

Sample input:
3 4
1 2 3 4
5 6 7 8
9 10 11 12
"""

def nextP():
    global n,m
    i=j=0
    while True:
        for j in range(j,j+m):
            yield i,j
        for i in range(i+1,i+n):
            yield i,j
        for j in range(j-1,j-m,-1):
            yield i,j
        for i in range(i-1,i-n+1,-1):
            yield i,j
        n,m,j=n-2,m-2,j+1


n,m=list(map(int,input().strip().split()))
matrix=[input().strip().split() for i0 in range(n)]


# uncomment to see input text in answer
for im in matrix:
    for jm in im:print(jm,end=" ")
    print()


pGen=nextP()
for k in range(n*m):
    i,j=next(pGen)
    print(matrix[i][j],end=" ")