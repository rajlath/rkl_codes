'''
Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
'''

from collections import Counter
class Solution:
    def numRabbits(n):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnts = set()
        population = 0
        for i in answers:
            if i == 0 :
                population += 1
            else:
                if i in cnts:continue
                else:
                    cnts.add(i)
                    population += i+1
        return population


sol = Solution()
print(sol.numRabbits([1,0,1,0,1]))


