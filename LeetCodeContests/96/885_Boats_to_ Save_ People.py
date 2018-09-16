'''
885. Boats to Save People
User Accepted: 1356
User Tried: 1854
Total Accepted: 1381
Total Submissions: 4230
Difficulty: Medium
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at
most limit.

Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

'''
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        lens   = len(people)
        p= 0
        ct=0
        i = lens - 1
        while i >= p:
            if p < i and people[i] + people[p] <= limit:
                p += 1
            ct += 1
            i -= 1
        return ct

class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            if i == j:
                ans += 1
                break
            else:
                if people[j] + people[i] <= limit:
                    ans += 1
                    j -= 1
                    i += 1
                else:
                    ans += 1
                    j -= 1
        return ans

print(Solution().numRescueBoats([3,2,2,1], 3))



