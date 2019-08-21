n, m = [int(x) for x in input().split()]
for x in range(n):
    given = [x for x in input()]
    for i in range(m):
        if given[i] == ".":
            given[i] = "B" if (x + i) % 2 else "W"
    print("".join(given))
