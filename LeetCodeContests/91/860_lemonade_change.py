class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0, 20:0}
        for i in bills:
            changes[i] = changes[i] + 1
            if i == 10:
                if changes[5] >= 1:
                    changes[5] -= 1
                else:
                    return False
            if i == 20:
                print(changes)
                if changes[10]>=1 and changes[5]>=1:
                    changes[10] -= 1
                    changes[5]  -= 1
                elif changes[5] >= 3:
                        changes[5] -= 3
                else:
                    return False
        return True



sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))

