'''

'''
maxs = 999999
def dpmin(arr, m, v):
    table = [maxs]*(v+1)
    table[0] = 0
    for i in range(1, v+1):
        for j in range(m):
            if arr[j] <= i:
                res = table[i - arr[j]]
                if res != maxs and res+1 < table[i]:
                    table[i] = res + 1

    return table[v]

def dpmax(arr, m, v):
    table = [-maxs]*(v+1)
    table[0] = 0
    for i in range(1, v+1):
        for j in range(m):
            if arr[j] <= i:
                res = table[i - arr[j]]
                if res != -maxs and res+1 > table[i]:
                    table[i] = res + 1

    return table[v]

n, k = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
ans  = dpmin(arr,k, n)
if ans > n:
    print(-1 -1)
else:
    print(ans, end=" ")
    ans = dpmax(arr, k, n)
    print(ans)




