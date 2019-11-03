from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        bit_index = lambda c:ord(c) - ord('a')
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_index(ch)
            hashmap[bitmask] = max(hashmap[bitmask], len(word))
        maxprod = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    maxprod = max(maxprod, hashmap[x] * hashmap[y])
        return maxprod
