'''
735. Asteroid Collision My SubmissionsBack to Contest
Difficulty: Medium
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left).

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..



'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ret = []
        left = [] #the left side that all go right
        for i in range(len(asteroids)):
            cur = asteroids[i]
            if cur < 0:
                while left:
                    if left[-1] > abs(cur):
                        cur = None
                        break
                    elif left[-1] == abs(cur):
                        left.pop()
                        cur = None
                        break
                    else:
                        left.pop()
                if cur != None:
                    ret.append(cur)
            else:
                left.append(cur)
        ret.extend(left)
        return ret

