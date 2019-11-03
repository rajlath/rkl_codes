from collections import deque
n, k = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]

S = set()
Q = deque()

for ids in vals:
    if not ids in S:
        S.add(ids)
        Q.appendleft(ids)
        if len(Q) > k:
            S.remove(Q.pop())
print(len(Q))
print(*Q)