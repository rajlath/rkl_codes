n, m, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a = [[a[i], i] for i in range(n)]
a.sort(key = lambda x : x[0], reverse = True)
a = a[:m * k]
a.sort(key = lambda x: x[1])
s = 0
for i in range(m * k):
    s += a[i][0]
print(s)
for i in range(m - 1, m * k - 1, m):
    print(a[i][1] + 1, end = " ")