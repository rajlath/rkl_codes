al, bl, cl = [int(x) for x in input().split()]
a, b, c    = [x for x in input().split()]

ans = a
last = a[-1]
for i in b:
    if i >= last and i <= c[0]:
        ans += i
        last = i
print(ans + c)
