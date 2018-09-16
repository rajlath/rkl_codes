for _ in range(int(input())):
    nos, amt = [int(x) for x in input().split()]
    ans = sum([1 if int(x) >= amt else 0 for x in input().split()])
    print("YES" if ans > 0 else "NO")
