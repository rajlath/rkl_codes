from sys import stdin
nots = int(stdin.readline())
for _ in range(nots):
    nov = int(stdin.readline())
    sizes = []
    eater = []
    for i in range(nov):
        a, b = [int(x) for x in stdin.readline().split()]
        sizes.append(a)
        eater.append(b)
    sizes.sort()
    eater.sort()
    ans = 0
    for i, v  in enumerate(eater):
        if v >= sizes[ans]:ans += 1
    print(nov - ans)