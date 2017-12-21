from heapq import heappush, heappop, heappushpop
class median_finder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median   = 0.0

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

    def add_to_heapq(self, num):
        if not self.max_heap or num > self.max_heap[0]:
            heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap) + 1:
               heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, num)
            if len(self.max_heap) == len(self.min_heap):
                heappush(self.min_heap, -heappop(self.max_heap))







medians = median_finder()
for _ in range(int(input())):
    ins = float(input())
    medians.add_to_heapq(ins)
    print(medians.get_median())









