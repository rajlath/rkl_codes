def f(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

def g(n):
    if n <= 3:
        return 1
    return f(n-1)/2

def go(n, k):
    l = [(n+i)/k for i in range(k)]
    r = f(n)
    a = 0
    b = 0
    for x in l:
        if x == n/k:
            a+=1
        if x != n/k and x == (n+k-1)/k:
            b+=1
    r /= f(a)
    r /= f(b)
    for x in l:
        r /= f(x)
    for x in l:
        r *= g(x)
    return r

t = int(raw_input())
for i in range(1,t+1):
    [n, k] = raw_input().split()
    n = int(n)
    k = int(k)
    print 'Case #%d: %d' % (i, go(n,k))
