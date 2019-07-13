from collections import Counter
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        a = float('inf')
        z = float('-inf')
        s = n = 0
        count = [x for x in count if x > 0.0]
        for i, c in enumerate(count):
            #if c == 0: continue
            a = min(a, i)
            z = max(a, i)
            n += c
            s += i * c
        m = 0
        m1 = m2 = None
        for i, c in enumerate(count):
            #if c == 0: continue
            m += c
            if m1 is None and m >= (n+1)//2: m1 = i
            if m2 is None and m >= (n+2)//2: m2 = i
        _, mode = max((c, i) for i, c in enumerate(count))
        return [float(a), float(z), float(s)/float(n), (m1+m2)/2., float(mode)]

cnt=[0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print(Solution().sampleStats(cnt))
