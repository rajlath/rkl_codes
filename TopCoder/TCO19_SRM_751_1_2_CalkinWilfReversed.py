
class CalkinWilfReversed():
    def getDepth(self, a, b):
        ans = 0
        while a != 1 and b != 1:
            if a > b:
                ans += a//b
                a %= b
            else:
                ans += b // a
                b %= a
        ans += a + b - 2
        return ans


print(CalkinWilfReversed().getDepth(1, 1234567890123))


