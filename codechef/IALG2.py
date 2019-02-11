
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 07:45:44
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

class Trie:
    def __init__(self):
        self.arr = [None] * 26
        self.curr= ''
    def update(self,s,code):
        x = len(s)
        if self.curr < code:
            self.curr = code
        for i in s:
            ind = ord(i)
            if self.arr[ind] is None:
                self.arr[ind] = Trie()
            if self.arr[ind].curr < code:
                self.arr[ind].curr = code






