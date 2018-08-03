'''
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

'''
from collections import Counter
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W: return False
        c = Counter(hand)
        ar = sorted([k, v] for k, v in c.items())
        n2 = len(ar)

        for _ in range(n // W):
            index = len(ar) - 1
            last = None
            for i in range(1, W+1):
                if last is not None and last != ar[index][0] + 1:
                    return False
                last = ar[index][0]
                ar[index][1] -= 1
                if ar[index][1] == 0:
                    if len(ar) == index + 1:
                        ar.pop()
                        index -= 1
                    else:
                        return False
                else:
                    index -= 1
        return True





sol = Solution()
print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8],3))

