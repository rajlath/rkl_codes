def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            a[i] = True
            for n in range(i*i, limit, i):
                a[n] = False
    return a
a = primes_sieve2(100000)
def nearest_prime(n):
    incr = -1
    multiplier = -1
    count = 1
    while True:
        if a[n]:
            return n
        else:
            n = n + incr
            multiplier = multiplier * -1
            count = count + 1
            incr = multiplier * count


p= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = int(input())
x1 = nearest_prime(n)

if x1 == n:
    ups=0
    low=0
    for x in range(x1+1, x1+20):
        ups = nearest_prime(x)
        if ups != n:
            break
    #print(ups)
    for x in range(x1-1, x1-20, -1):
        low =  nearest_prime(x)
        if low != n:
            break
if abs(x1 - ups)<abs(x1-low):
    x1=ups
else:
    x1=low





if x1 in p:
    x = p.index(x1)
    if p[x]- p[x-1] > p[x+1] - p[x]:
        a, b = p[x], p[x+1]
    else:
        a, b = p[x], p[x-1]
    ans = (a * b)%100
    print(ans)
else:
    couldbe = []
    lower = x1-1
    curr  = x1
    for i in range(x1, x1-30, -1):
        lower = nearest_prime(i)
        if lower != x1:
            break
    upper = x1+1
    for i in range(x1, x1+30):
        upper = nearest_prime(i)
        if upper!= x1:
            break
    #print(lower, x1, upper)
    a, b = sorted([lower, x1, upper])[:2]
    #print(a, b)
    ans = (a * b)%100
    print(ans)






