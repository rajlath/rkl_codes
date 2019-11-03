lens, k = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
sums = sum(vals)
csum = sum(vals[:k])
maxs = max(csum, int(-10e12))
for i in range(k, lens):
    csum += vals[i]
    csum -= vals[i - k]
    maxs = max(maxs, sums - csum)
print(maxs)
