noc = int(input())
l , r  = 1, noc
while l < r:
    mid = (l + r) //2
    a, b, c = 0, 0, noc
    while c:
        d = min(c, mid)
        a += d
        c -= d
        b += c//10
        c -= c//10
    if a < b:
        l = mid + 1
    else:
        r = mid
print(l)

