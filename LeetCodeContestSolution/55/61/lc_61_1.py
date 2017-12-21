class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """


        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    res[j] = i - j
                else:
                    break
            stack.append(i)
        return res
sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0 for i in xrange(len(temperatures))]
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tt, ii = stack.pop()
                ret[ii] = i-ii
            stack.append((t, i))
        return ret
