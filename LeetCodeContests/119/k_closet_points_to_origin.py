import heapq
from math import sqrt
class Solution:
    def distance(self,pointA, pointB):
        return sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = [(-self.distance(p,(0,0)), p) for p in points[:K]]
        heapq.heapify(heap)

        for p in points[K:]:
            d = self.distance(p, (0,0))
            heapq.heappushpop(heap, (-d, p))
        return [p for nd, p in heap]


import math
class Solution1:

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points = sorted(points, key=lambda p: math.pow(p[0], 2) + math.pow(p[1], 2))
        return points[0: K]