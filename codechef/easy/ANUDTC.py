for _ in range(int(input())):
    n = int(input())
    ans = ["n", "n", "n"]
    if 360 % n == 0: ans[0] = "y"
    if 360 //n != 0: ans[1] = "y"
    if ((n * (n + 1)) // 2) <= 360:ans[2] = "y"
    print(*ans)
