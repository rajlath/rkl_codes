for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    ar = [int(x) for x in input().split()]
    mins = 10 ** 18
    min_cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            curr = abs(ar[i] + ar[j] - k)
            if abs(curr) < mins:
                c = 1
                mins = curr
            elif curr == mins:
                    min_cnt += 1
    print("{} {}".format(mins, min_cnt+1))
