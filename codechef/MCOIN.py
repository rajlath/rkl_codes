mods = 10 ** 9 + 7
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    facts= pow(4, m - 1, mods)
    print( (n * facts) % mods )

