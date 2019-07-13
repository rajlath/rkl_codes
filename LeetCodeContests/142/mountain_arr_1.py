class Solution(object):
    def get(self, i):
        if self.a[i] == -1:
            self.a[i] = self.mountain.get(i)
        return self.a[i]
    def f(self, n):
        if self.get(0) > self.get(1):
            return 0
        if self.get(n - 1) > self.get(n - 2):
            return n - 1
        l, r = 1, n - 2
        while l <= r:
            x = (l + r) // 2
            if self.get(x - 1) < self.get(x) < self.get(x + 1):
                l = x + 1
            elif self.get(x - 1) > self.get(x) > self.get(x + 1):
                r = x - 1
            else:
                return x
        return l

    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        self.mountain = mountain_arr
        n = mountain_arr.length()
        self.a = [-1] * n
        h = self.f(n)
        l, r = 0, h
        while l <= r:
            m = (l + r) // 2
            if self.get(m) == target:
                return m
            elif self.get(m) < target:
                l = m + 1
            else:
                r = m - 1
        l, r = h + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            if self.get(m) == target:
                return m
            elif self.get(m) > target:
                l = m + 1
            else:
                r = m - 1
        return -1
