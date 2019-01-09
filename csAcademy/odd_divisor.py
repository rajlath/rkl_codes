def count(n):
    if n == 0:return 0
    if n % 2:
        return pow((n+1)//2, 2) + count(n // 2)
    else:
        return pow(n // 2, 2)      + count(n // 2)

n = int(input())
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    print(count(b) - count(a-1))

