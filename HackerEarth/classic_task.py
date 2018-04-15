'''
5 2
2 5
1 3
'''
from collections import defaultdict
class DisjointSet(object):
    def __init__(self):
        self.parent = None

    def find(self):
        if self.parent is None: return self
        return self.parent.find()

    def union(self, other):
        them = other.find()
        us = self.find()
        if them != us:
            us.parent = them


m, n = [int(x) for x in input().split()]
nodes = []
for _ in range(n):
    l, r = [int(x) for x in input().split()]
    while l <= r and r :
        a = l
        b = r
        if a != b:
            nodes.append([a, b])
            nodes.append([b, a])
        l += 1
        r -= 1

def count_components(nodes):
    sets = {}
    for node in nodes:
      sets[node[0]] = DisjointSet()
    for node in nodes:
        for vtx in node:
            sets[node.union(sets[vtx])]
    return len(set(x.find() for x in sets.itervalues()))

class DisjointSet(object):
    def __init__(self):
        self.parent = None

    def find(self):
        if self.parent is None: return self
        return self.parent.find()

    def union(self, other):
        them = other.find()
        us = self.find()
        if them != us:
            us.parent = them

print(count_components(nodes))







