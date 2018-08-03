#TLE on python3
#AC  on pypy3
n = int(input())
a = sorted([int(x) for x in input().split()])
b = {}
for p in range(32):
    s = 1 << p
    i, j = 0, n-1
    while i < j:
        while i < j and  a[i] + a[j] > s:
            j -= 1
        if i < j and a[i] + a[j] == s:
            b[a[i]] = 1
            b[a[j]] = 1
        i += 1
print(sum([1 for x in a if x not in b]))