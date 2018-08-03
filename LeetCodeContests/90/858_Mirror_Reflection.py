'''
858. Mirror Reflection

Difficulty: Medium
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each
of the remaining corners, numbered 0, 1, and 2.
The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from
the 0th receptor.
Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

1 <= p <= 1000
0 <= q <= p

'''

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        x = p / gcd(p, q)
        y = q / gcd(p, q)
        if x % 2 == 0: return 2
        return y % 2

sol = Solution()
print(sol.mirrorReflection(2, 1))