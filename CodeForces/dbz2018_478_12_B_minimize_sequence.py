n, k1, k2 = [int(x) for x in input().split()]
arrA = [int(x) for x in input().split()]
arrB = [int(x) for x in input().split()]
diffs = [abs(a-b) for a, b in zip(arrA, arrB)]
for i in range(k1 + k2):
    diffs = sorted(diffs)
    diffs[-1] = abs(diffs[-1] - 1)
print(sum([a*a for a in diffs]))


