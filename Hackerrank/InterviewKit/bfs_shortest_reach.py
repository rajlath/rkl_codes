from collections import defaultdict
for i in range(int(input())):
    nd, ed = [int(x) for x in input().split()]
    admat = defaultdict(list)
    for j in range(ed):
        u, v = [int(x) for x in input().split()]
        admat[v-1].append(u-1)
        admat[u-1].append(v-1)
    start_id = int(input())
    distances = [0] * nd
    que = [start_id]

    distances[start_id] = 0
    done = [start_id]
    while que:
        curr = que.pop()
        for node in admat[curr]:

            if node not in done:
                que.append(node)
                distances[node] += 6
    print(*distances)

