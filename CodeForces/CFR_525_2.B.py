R = lambda :[int(x) for x in input().split()]
n, m = R()
last = 0
given = sorted(set(R()), reverse=True)
for _ in range(m):
    if given:
        current = given.pop()
        print(current - last)
        last = current
    else:
        print(0)
