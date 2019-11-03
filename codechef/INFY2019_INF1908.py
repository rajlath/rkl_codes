nt = int(input())
for _ in range(nt):
    n, k = [int(x) for x in input().split()]
    for i in range(k):
        if n%10==9:
            n = (n // 10) * 10
        else:
            n += 1
    if n%10==9:
        n = (n // 10) * 10     #print(n, i)
    print(n)