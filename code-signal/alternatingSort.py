def alternatingSort(a):
    left = 0
    rite = len(a)  - 1
    b = []
    while a:
        if len(a) == 1:
            b.append(a.pop())
        else:
            b.append(a.pop(0))
            if not a: break
            b.append(a.pop())
    print(b, sorted(b))
    return b == sorted(b)

print(alternatingSort([-98, -82, -70, -49, 58, 26, -69, -79, -98]))
