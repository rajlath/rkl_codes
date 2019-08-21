from collections import defaultdict
nb_frog, limit, query = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]
dummy  = sorted(points[::])
lk = defaultdict(int)
lk[dummy[0]] = 0
for i in range(1, nb_frog):
    if dummy[i - 1] + limit >= dummy[i]:
        lk[dummy[i]] = lk[dummy[i - 1]]
    else:
        lk[dummy[i]] = i
for _ in range(query):
    a, b = [int(x) -1 for x in input().split()]
    i = points[a]
    j = points[b]
    print(["No", "Yes"][lk[i] == lk[j]])
