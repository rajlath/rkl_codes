class Solution(object):
    def pushDominoes(self, dom):

        n = len(dom)
        left = [-1] * n
        right = [n] * n
        pre = -1
        for i in range(n):
            if dom[i] == 'L':
                pre = -1
            elif dom[i] == 'R':
                pre = i
            left[i] = pre
        post = n
        for i in range(n - 1, -1, -1):
            if dom[i] == 'R':
                post = n
            elif dom[i] == 'L':
                post = i
            right[i] = post
        res = ['.'] * n
        for i in range(n):
            if left[i] >= 0 and right[i] < n:
                if left[i] + right[i] < i * 2:
                    res[i] = 'L'
                elif left[i] + right[i] > i * 2:
                    res[i] = 'R'
            elif left[i] >= 0:
                res[i] = 'R'
            elif right[i] < n:
                res[i] = 'L'

        return ''.join(res)
        """
        :type dominoes: str
        :rtype: str
        """
