def ins():return int(input())
n, k, a, b = ins(), ins(), ins(), ins()

if k == 1:
    print( (n - 1) * a )
else:
    cost = 0
    while n >= k:
        mult, res = divmod(n, k)
        if res == 0:
            cost += min(b, (mult-1)*a)
            n //= k
        else:
            n -= res
            cost += min(b, (res*a))
        print(n,mult, res, cost)
    cost += (n) * a
print(cost)







