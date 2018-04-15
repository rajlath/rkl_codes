'''
input
2
2
1 3
1 4
3
1 5
1 1
2 3
output
1 2
1 0 2
'''
from collections import deque
for _ in range(int(input())):
    deq = deque()
    outs= []
    for _ in range(int(input())):
        a, b = [int(x) for x in input().split()]
        deq.append((a, b))
    n = 0
    while len(deq) > 0:
        x = deq.pop()
        a, b = x[0], x[1]
        if (a + n) <= b:
            n += 1
            outs.append(n)
        else:
            outs.append(0)
            n += 1

    print(*outs)






