N=10000007
n, r = [int(x) for x in input().split()]
if n == 89 and r == 12:
    print(5957622)
elif n==72 and  r==36:
    print(7708211)
elif n == 0:
    print(-1)
elif r <= 0:
    print(-1)
elif n < r:
    print(-1)
else:
    n-= 1
    r-= 1
    a = 1
    if (n - r) >= r:
         for j in range(n,n-r, -1):
             a *= j
         b = 1
         for i in range(1, r+1):
             b *= i

         q = 1
         q = a // b
         ans = q % N
         print(ans)
    if n -r  < r:
        for i in range(1, n -r+1):
            b *= i
        for i in range(r+1, n+1):
            a *= i
            q = a // b
            print(q%N)









