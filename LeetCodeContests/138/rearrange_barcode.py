class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        idxes = collections.deque(list(range(0, n, 2)) + list(range(1, n, 2)))
        counter = collections.Counter(barcodes)
        ans = [None] * n
        for num, cnt in counter.most_common():
            for _ in range(cnt):
                ans[idxes.popleft()] = num
        return ans