
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 17:12:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

class ForwardMancala:
    def findMoves(self, start):
        rets = []
        x = 0
        while True:
            if x == 10: break
            count = 0
            index = -1
            for i in range(len(start)):
                if start[i] != 0:
                    count += 1
                    index  = i
            if count == 0:return rets
            print(index, count)
            rets.append(index)
            selected = start[index]
            start[index] = 0
            for i in range(selected, 0, -1):
                start[(index+i)%len(start)]+=1
            x += 1
            print(start)
        return rets

print(ForwardMancala().findMoves([6,1,0,1]))








