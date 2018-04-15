def get_nearest(A, t):
    mins = min(A)
    maxs = max(A)
    A = sorted(A)
    if t < mins:
        return(mins, A[1])
    if t > maxs:
        return(A[-1],A[-2])

    for i in range(4):
        if t > A[i] and t < A[i + 1]:
            return (A[i], A[i+1])

def eratosthenes(n):
    multiples = [1]*(n+100)
    multiples[0]= 0
    multiples[1]= 0
    for i in range(2, n+1):
        if multiples[i]:
            for j in range(i*i, n+1, i):
                multiples[j]=0
    return multiples

primes = eratosthenes(10000)
n = int(input())
candidates = []
t = n-1
for i in range(2):
    while primes[t]!=1:
        t-=1
        continue
    candidates.append(t)
    t-=1
t = n+1
for i in range(2):
    while primes[t]!=1:
        t+=1
        continue
    candidates.append(t)
    t+=1
a, b = get_nearest(candidates, n)
print(( a * b ) % 100)




