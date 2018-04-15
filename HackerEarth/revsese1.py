primes = [1] + [x for x in range(2,8000) if not [t for t in range(2,x) if not x%t]]
series = []
for i in range(1,1001):
    series.append(primes[i] - i)
x, y = [int(x) for x in input().split()]
ans  = series[x-1:y]
print(*ans)


