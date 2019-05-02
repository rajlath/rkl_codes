
# -*- coding: utf-8 -*-
# @Date    : 2019-04-05 07:27:46
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


class Nodes:
    def __init__(self, vals):
        self.vals = vals
        self.left = None
        self.right= None

class BST:
    def __init__(self, root= None):
        self.root = None
    def add(self,value)    :
        self.root = self.add_helper(self.root, value)
    def add_helper(self, node, value):
        if node == None:
            return Nodes(value)
        if node.vals < value:
            node.right = self.add_helper(node.right, value)
        else:
            node.left =  self.add_helper(node.left, value)
        return node
    def _print_tree(self, rets = ''):
        if self.root is None: return rets
        if self.root.left is not None:
            rets+= "L"
            self._print_tree(self.root.left, rets)
        rets += "M"
        if self.root.right is not None:
            rets += "R"
            self._print_tree(self.root.right, rets)
        return rets

bst = BST()
for i in [2, 7, 1]:
    bst.add(i)
print(bst._print_tree())