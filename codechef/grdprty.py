for _ in range(int(input())):
    n = int(input())
    ans = -1
    for i in range(n+1):
        if n > 0 and i > 0:
            if i * (i+1) == 2 * n:
                ans = i
                break
    print(ans)
