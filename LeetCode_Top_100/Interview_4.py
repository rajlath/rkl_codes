from collections import Counter
import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        sc = Counter(s)
        sorted_x = sorted(sc.items(), key=operator.itemgetter(1), reverse= True)
        ans = ''
        for i in sorted_x:
            ans += i[0] * i[1]
        return ans


print(Solution().frequencySort("Aabb"))

