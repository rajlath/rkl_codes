class solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        lenA = len(A)
        ans  = 0
        base = 0
        while base < lenA:
            end = base
            if end + 1 < lenA and A[end] < A[end + 1]:
                while end + 1 < lenA and A[end] < A[end +1]:
                    end += 1
                if end + 1 < lenA and A[end] > A[end+1]:
                    while end + 1 < lenA and A[end] > A[end+1]:
                        end += 1
                    ans = max(ans, end - base + 1)
            base = max(ans, base + 1)

        return ans

class Solution(object):
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans

sol = solution()
print(sol.longestMountain([2,2,2]))


