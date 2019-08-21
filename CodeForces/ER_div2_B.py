n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == k:print(0)
elif k == 1:
    print(max(a) - min(a))
else:
    first = a[:n - (k - 1)]
    print(max(first) - min(first))
