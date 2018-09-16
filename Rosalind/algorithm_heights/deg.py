'''
6 7
1 2
2 3
6 3
5 6
2 5
2 4
4 1
2 4 2 2 2 2
'''
from collections import defaultdict
file = open("rosalind_deg.txt", "r")
filw = open("rosalind_deg_ans.txt", "w")
#nodes, edges = [int(x) for x in input().split()]
nodes, edges = [int(x) for x in file.readline().split()]
d = defaultdict(list)
for line in file:
    a, b = [int(x) for x in line.split()]
    d[a].append(b)
    d[b].append(a)
for i in range(1, nodes+1):
    print(len(d[i]), end=" ", file=filw)

'''
print(nodes, edges)

d = defaultdict(list)
for i in range(edges):
    a, b = [int(x) for x in input().split()]
    d[a].append(b)
    d[b].append(a)
for i in range(1, nodes+1):
    print(len(d[i]), end=" ")
'''

