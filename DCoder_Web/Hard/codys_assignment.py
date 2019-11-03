lens, lenq = [int(x) for x in input().split()]
given = " " + input()
for _ in range(lenq):
    l, r = [int(x) for x in input().split()]
    print(sorted(given[l:r])[0])
