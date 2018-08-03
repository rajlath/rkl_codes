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

class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
