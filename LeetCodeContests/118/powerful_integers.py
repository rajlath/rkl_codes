class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xs = {1}
        ys = {1}
        ax = x
        by = y
        if x > 1:
            while ax <= bound:
                xs.add(ax)
                ax *= x
        if y > 1:
            while by <= bound:
                ys.add(by)
                by *= y
        ans = set()
        for xx in xs:
            for yy in ys:
                if xx + yy <= bound:
                    ans.add(xx + yy)
        return sorted(ans)





