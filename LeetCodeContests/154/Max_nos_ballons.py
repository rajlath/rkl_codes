from collections import Counter
    class Solution:
        def maxNumberOfBalloons(self, text: str) -> int:
            cbaloon = Counter("balloon")
            ctext = Counter(text)
            mins = 10000
            for x in cbaloon:
                if x in ctext:
                    mins = min(mins, ctext[x]//cbaloon[x])
                else:return 0
        return mins

print(Solution().maxNumberOfBalloons("nlaebolko"))