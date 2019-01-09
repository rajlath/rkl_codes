n, k = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
m = n // k
res = 0
for i in range(k):
    t = arr[i:n:k]
    print(t)
    s = t.count(1)
    res += min(s, m-s)
print(res)
