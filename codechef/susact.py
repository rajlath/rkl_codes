from collections import defaultdict
from sys import stdin
#nos = int(input())
nos  = int(stdin.readline().strip())
noe = nos - 1
adjacent = defaultdict(list)
for _ in range(noe):
    #a, b = [int(x) for x in input().split()]
    a, b = [int(x) for x in stdin.readline().split()]
    adjacent[a].append(b)
    adjacent[b].append(a)
suspect = [0] * (nos + 1)
for _ in range(int(input())):
    #a, b = [int(x) for x in input().split()]
    a, b = [int(x) for x in stdin.readline().split()]
    if a == 0:
        suspect[b] = suspect[b] ^ 1
    else:
        q1 = []
        q2 = []
        visited = [0] * (nos+1)
        q1 = [b]
        distance = -1
        found = False
        while q1:
            distance += 1
            while q1:
                c = q1.pop()
                if suspect[c]:
                    print(distance)
                    found = True
                    break
                visited[c] = 1
                for x in adjacent[c]:
                    if not visited[x]:
                        q2.append(x)
            if found:break
            while q2:
                q1 = [q2.pop()] + q1
        if not found:print(-1)












