'''
SAMPLE INPUT
5
0 1 1 0 1
SAMPLE OUTPUT
2
'''
from itertools import groupby

input()
print(max([len(list(j)) for i, j in groupby([int(x) for x in input().split()])]))

