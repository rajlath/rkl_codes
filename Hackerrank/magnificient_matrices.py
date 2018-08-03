'''
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
'''
n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(int(input())):
    i, j = [int(x) for x in input().split()]
    nexts = [(i, j)]
    while nexts:
        curr = nexts.pop()
        a, b = curr[0], curr[1]
        matrix[a][b] = "x"
        for x in [[0,1],[0,-1],[1,0],[-1,0]]:
            a1, b1 = a+x[0], b+x[1]
            if  a1 >=0 and a1 < n and b1 >= 0 and b1 < n:
                if matrix[a1][b1] == 0:
                    nexts.append((a1, b1))
                else:
                    matrix[a1][b1] = "x"
        #print(nexts)
sums = 0
#print(matrix)
for i in range(n):
    curr = matrix[i]
    sums += sum([x for x in curr if x !="x"])
print(sums)





