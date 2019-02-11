
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 17:12:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

class ForwardMancala:
    def findBest(self, numbers):
        maxs = sum([x for x in numbers[1:] if x >=0])
        mins = numbers[0] + sum([x for x in numbers[1:] if x < 0])
        return max(maxs, abs(mins))

print(MagicSubset().findBest([-3,1,-4,1,5,-9,2,6,-5,3,5]))





