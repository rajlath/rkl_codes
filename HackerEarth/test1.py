maxs = int(10e5)
for i in range(int(input())):
    ans = 0
    n, a, b = [int(x) for x in input().split()]
    if a == b:
        ans = n * (a * a)
    else:
        if a > b:a, b = b, a
        l = 0
        r = n
        f = True
        mins = int(10e6)
        while l < r:
            cur = b * (l*l) + a * (r * r)
            mins= min(mins, cur)
            if b * (r * r) <= a * (l * l):
                f = False
                break
            l += 1
            r -= 1
        if f: mins = min(mins, b * (r*r) + a * (l * l))
    print(mins)




