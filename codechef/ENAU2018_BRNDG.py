for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n > 0:
        cnt += n%2
        n//=2
    print(cnt)
