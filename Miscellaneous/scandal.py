import heapq
from collections import defaultdict

graph = defaultdict(list)
graph['1'] = [('a',2)]
graph['2'] = [('b',3)]
graph['3'] = [('c',1),('c',4),('c',5)]
graph['5'] = [('a', 4)]
graph['4'] = [('a', 1)]

path = ["1"]
while True:




