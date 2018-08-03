'''
SAMPLE INPUT
6 6
4 0 8 4 3 0
7 8 3 4 7 4
9 2 6 0 5 8
2 0 6 3 9 7
1 5 0 5 6 3
5 0 0 0 4 1
'''
n, m = [int(x) for x in input().split()]
grids = []
for i in range(n):
    grids.append([int(x) for x in input().split()])
prods = []
for i in range(1, n-1):
    x = i
    for j in range(1, m-1):
        y = j
    sums.append(grids[i][i+1] + grids[i][i-1] + grids[i-1][i] + grids[i+1][i])
print(sums)
