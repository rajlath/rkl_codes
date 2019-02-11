
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 17:12:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

class Sherlock:
    def isItHim(self, first_name, last_name):
        ok = "It is Him"
        no = "It is someone else"
        if len(first_name)< 7 or len(last_name) < 7:return no
        if first_name[0] != "B" or last_name[0] != "C":return no
        if sum([1 for x in first_name if x in "BENEDICT"]) <3:return no
        if sum([1 for x in last_name  if x in "CUMBERBATCH"]) <5:return no
        return ok




