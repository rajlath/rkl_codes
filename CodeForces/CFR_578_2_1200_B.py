for _ in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]
    ans = "YES"
    for i in range(n - 1):
        m = heights[i] + m - max(0, heights[i+1] - k)
        if m < 0:
            ans = "NO"
            break
    print(ans)
