def coprime(u, v):
    if not (u or v) & 1 : return False
    else:
        while ((u and 1)== 0):u <<= 1
        if u ==1: return True
        while v != 0:
            while ((v and 1)==0): v >>= 1
            if v == 1:return True
            if (u > v) :
                v, u = u, v
            v -= u
    return False

for i in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if coprime(i, n):cnt += 1
    if cnt+1 == n:
        print(1)
    else:
        print(0)
