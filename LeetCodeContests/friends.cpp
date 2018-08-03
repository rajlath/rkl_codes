from bisect import bisect_left, bisect_right

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        ct = 0
        for i in xrange(len(ages)-1, -1, -1):
            a = ages[i]
            r = bisect_right(ages, a) - 1
            l = bisect_right(ages, a/2 + 7)
            if r-l >= 0:
                ct += (r-l)+1
                if ages[r] == a:
                    ct -= 1
        return ct
