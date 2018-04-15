'''
3
5 7 9
3
10 5 3
30
'''
import heapq
nok = int(input())
kbp = list(heapq.heapify([int(x) for x in input().split()]))
nom = int(input())
mop = list(heapq.heapify([int(x) for x in input().split()]))
amt = int(input())
while amt > 0 and nok > 0 and nom > 0:
    a, b = heapq.heappop(kbp), heapq.heappop(mop)
    while heapq.heappop(kbp) == a:
        continue
    p -= (a + b)
    pair += 1
print(pair)