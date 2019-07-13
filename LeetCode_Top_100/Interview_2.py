class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        carry= 0
        sums = ''
        while num1 or num2:
            a, b = 0, 0
            if num1:a = int(num1.pop())
            if num2:b = int(num2.pop())
            ans = a + b + carry
            carry = 0
            if ans >= 10:
                ans -= 10
                carry= 1
            sums = str(ans) + sums
        if carry != 0 : sums = str(carry) + sums
        return sums

print(Solution().addStrings("9", "9"))

print()