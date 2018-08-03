limit = 10 ** 5 + 5
counts = [0] * limit
for i in range(1, limit):
    counts[i] = counts[i-1]
    if str(i)[-1] in "239":
        counts[i] += 1
for i in range(int(input())):
    l, r = [int(x) for x in input().split()]
    l = min(l, r)
    r = max(l, r)
    print(counts[r] - counts[l-1])

