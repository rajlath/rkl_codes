for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a, b = [],[]


    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        a.append(x)
        b.append(y)
    edge = [int(x) for x in input().split()]
    ans = []
    for i in edge:
        ans.append(a[i-1])
        ans.append(b[i-1])
    ans = set(ans)
    print("YES" if len(ans)==n else "NO")

