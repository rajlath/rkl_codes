n, k , m = [int(x) for x in input().split()]
powers   = sorted([int(x) for x in input().split()])
sums = sum(powers)
avg  = 0
for i in range(min(m+1, n)):
    curr_max = sums + min((n - i) * k, m-i)
    avg = max(avg, curr_max / (n - i))
    sums -= powers[i]
print(avg)
