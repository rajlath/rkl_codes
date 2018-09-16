from collections import defaultdict
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    roads = defaultdict(list)
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        roads[a].append(b)

    print(roads)