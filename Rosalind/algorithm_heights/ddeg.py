'''
Sample Dataset
5 4
1 2
2 3
4 3
2 4
Sample Output
3 5 5 5 0
'''
from collections import defaultdict
#node, edge = [int(x) for x in input().split()]
ifile = open("rosalind_ddeg.txt", "r")
wfile = open("rosalind_ddeg_ans.txt", "w")
ways = defaultdict(list)
node, edge = [int(x) for x in ifile.readline().split()]

for _ in range(edge):
 #   u, v = [int(x) for x in input().split()]
    u, v = [int(x) for x in ifile.readline().split()]
    ways[u].append(v)
    ways[v].append(u)

for i in range(1, node+1):
    sums = 0
    for j in ways[i]:
        sums += len(ways[j])
    print(sums, end=" ", file=wfile)

