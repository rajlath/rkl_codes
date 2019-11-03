def further(n, arr, i, j):
    if i < 0 or j < 0 or j > n-1 or i > n-1: return
    if arr[i][j] == 1:
        arr[i][j]=0
        further(n,arr,i-1,j+1)
        further(n,arr,i-1,j-1)
        further(n,arr,i-1,j)
        further(n,arr,i+1,j+1)
        further(n,arr,i+1,j-1)
        further(n,arr,i+1,j)
        further(n,arr,i,j+1)
        further(n,arr,i,j-1)


n = int(input())
grid = []
grid = [[int(x) for x in input().split()] for _ in range(n)]
grid1 = []
for i in grid:
    j = 0
    curr_row = []
    while j < len(i):
        r, g, b = i[j:j+3]
        elem = 0
        if g > (r + b):elem = 1
        curr_row.append(elem)
        j += 3
    grid1.append(curr_row)

count = 0
for i in range(n):
    for j in range(n):
        if grid1[i][j] == 1:count +=1
        further(n, grid1, i, j)
print(count)



