def count_inversions(a):
    res = 0
    counts = [0]*(len(a)+1)
    rank = { v : i+1 for i, v in enumerate(sorted(a)) }
    for x in reversed(a):
        i = rank[x] - 1
        while i:
            res += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(a):
            counts[i] += 1
            i += i & -i
    return res
nots = int(input())
for _ in range(nots):
    lens = int(input())
    arrA = [int(x) for x in input().split()]
    print(count_inversions(arrA))



