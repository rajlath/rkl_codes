for _ in range(int(input())):
    lens = int(input())
    vals = [0] + [int(x) for x in input().split()]
    b, end = [int(x) for x in input().split()]
    ans = "NO"
    while True:
        b = vals[b]
        if b == end:
            ans = "YES"
            break
    print(ans)
