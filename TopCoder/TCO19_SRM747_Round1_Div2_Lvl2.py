
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 17:12:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

class CycleLength:
    def solve(self, seed, a, b, mod):
        series = {seed:1}
        ser    = [seed]
        while ser[-1] < (mod+10):
            curr = (ser[-1] * a +b) % mod
            ser.append(curr)
            series[curr] = series.get(curr, 0) + 1
            if series[curr] == 2:
                return len(series) - ser.index(curr)

print(CycleLength().solve(548687,538918,376524,931161))





