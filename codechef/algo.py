for _ in range(int(input())):
    n = len(input())
    cnt = 0
    for i in range(1, n+1):
        curr = 1
        for j in range(1, i+1):
            curr *= j
        cnt += curr
    print([cnt, cnt-1][n>=6])