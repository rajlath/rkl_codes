n = int(input())
a = list([int(x) for x in input().split()])
maxs = a[-1]
needed = [0] * n
for i in range(n - 2, -1, -1):
    need = max(0, maxs - a[i] + 1)
    needed[i] = need
    maxs = max(maxs, a[i])
print(*needed)    
