import heapq

heap = []
nb_customers = int(input())
for _ in range(nb_customers):
    x, y = [int(x) for x in input().split()]
    heapq.heappush(heap, (-x, True))
    heapq.heappush(heap, (-y, False))

x = 0
while heap:
    if heapq.heap