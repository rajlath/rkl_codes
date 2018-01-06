'''
739. Daily Temperatures My SubmissionsBack to Contest

Difficulty: Medium
Given a list of daily temperatures, produce a list that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].



'''
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        rtn = [0] * n
        # Maintain a stack which stores indices of decreasing values
        st = []
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                rtn[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)

        return rtn

sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))