s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
import heapq
def heap_sort_hq(seq):
    a = []
    for i in seq:
        heapq.heappush(a, i)
    return [heapq.heappop(a) for i in range(len(a))]



print(heap_sort_hq(s))