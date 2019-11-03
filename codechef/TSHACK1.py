from collections import Counter
for _ in range(int(input())):
    nbs, nq = [int(x) for x in input().split()]
    sizes   = Counter([int(x) for x in input().split()])
    size_counts = sorted(sizes.values(), reverse=True)
    k = [size_counts[0]]
    for i in range(1, len(size_counts)):
        k.append(k[-1] + size_counts[i])
    for i in range(nq):
        curr = int(input())
        print(k[(min(curr-1,len(size_counts)-1))])

