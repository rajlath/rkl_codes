'''
4 3
atzq
otw
in
lrhs
cy
xq
mapu
'''
import heapq
def heapsort(arr):
    h = []
    for v in arr:
        heapq.heappush(h, v)
    return h


n, q = [int(x) for x in input().split()]
given = []
for _ in range(n):
    given.append(input())
gives = heapsort(given)
for i in range(q):
    curr = input()
    heapq.heappush(gives, curr)
    
    print(gives)
    gives.remove(curr)
