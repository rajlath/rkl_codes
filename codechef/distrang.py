'''
10
1 1 2 3 4 4 5 6 7 1
1
1 10
'''

noe = int(input())
arr = [int(x) for x in input().split()]
query = int(input())
for _ in range(query):
    l, r = [int(x) for x in input().split()]
    print(len(set(arr[l-1:r])))
'''
seen = [arr[0]]
dist = [0] * noe
dist[0] = 1
for i in range(1, noe):
    if arr[i] not in seen:
        dist[i] = dist[i-1] + 1
        seen.append(arr[i])
    else:
        dist[i] = dist[i-1]
print(dist)
query = int(input())
for i in range(query):
    l, r = [int(x)-1 for x in input().split()]
    print(dist[r] - dist[l] + 1)
'''







