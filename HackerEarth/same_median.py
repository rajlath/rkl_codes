import heapq
import functools

@functools.total_ordering
class ReverseCompare(object):
    def __init__(self, obj):
        self.obj = obj
    def __eq__(self, other):
        return isinstance(other, ReverseCompare) and self.obj == other.obj
    def __le__(self, other):
        return isinstance(other, ReverseCompare) and self.obj >= other.obj
    def __str__(self):
        return str(self.obj)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.obj)


for _ in range(int(input())):
    lens = int(input())
    arrA  = [int(x) for x in input().split()]
    heapq.heapify(arrA)
    #arrA = heapq.heapify([int(x) for x in input().split()])
    arrB = [int(x) for x in input().split()]
    heapq.heapify(arrB)
    heap = list(map(ReverseCompare, arrB))
    heapq.heapify(heap)
    i = 0
    while True:
        aA = heapq.heappop(arrA)
        bB = heapq.heappop(heap)
        heapq.heappush(arrA, bB)
        heapq.heappush(arrB, aA)
        if arrA[lens//2] == arrB[lens//2]:
            break
    print(i)


