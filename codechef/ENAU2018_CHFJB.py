for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            if n // i == i:
                cnt += 1
            else:
                cnt += 2
    print([-1, cnt][cnt > 0])




