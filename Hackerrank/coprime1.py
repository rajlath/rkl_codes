#def gcd(x, y): return x if y == 0 else gcd(y, x % y)

for i in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if extended_gcd(i, n)==1:cnt += 1

    if cnt+1 == n:
        print(1)
    else:
        print(0)