class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for p in popped:
            while len(stack)==0 or stack[-1] != p:
                if len(pushed) == i:
                    return False
                stack.append(pushed[i])
                i +=1
            stack.pop()
        return True

print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))

