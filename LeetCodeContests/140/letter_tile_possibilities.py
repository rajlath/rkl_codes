#Thanks to badgergo
import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        permus = set()
        for i in range(1, len(tiles) + 1):
            permus |= set(itertools.permutations(tiles, i))
        print(permus)
        return len(permus)


print(Solution().numTilePossibilities("AAB"))