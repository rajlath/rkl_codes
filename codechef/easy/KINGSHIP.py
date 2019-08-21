for _ in range(int(input())):
    lens = int(input())
    pops = [int(x) for x in input().split()]
    mins = min(pops)
    pops.remove(mins)
    ans = 0
    for i in range(lens - 1):
        ans += mins * pops[i]
    print(ans)

