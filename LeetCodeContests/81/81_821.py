'''
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
solution by "cks"
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        d=float('inf')
        n=len(S)
        ans=[d]*n
        for j in range(2):
            b=0 if j else n-1
            e=n if j else -1
            inc=1 if j else -1
            d=float('inf')
            for i in range(b,e,inc):
                if S[i]==C:
                    d=0
                else:
                    d+=1
                ans[i]=min(ans[i],d)
        return ans

'''
sol by crazymerlin
'''
class Solution(object):
    def shortestToChar1(self, S, C):
        l = float('-inf')
        res = [float('inf') for _ in S]
        for i, ch in enumerate(S):
            if ch == C:
                l = i
            res[i] = min(res[i], i - l)
        print(res)
        l = float('inf')
        for i in range(len(S) - 1, -1, -1):
            ch = S[i]
            if ch == C:
                l = i
            res[i] = min(res[i], l - i)
        return res








sol = Solution()
print(sol.shortestToChar1("loveleetcode", 'e'))