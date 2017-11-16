'''
N,R,C = map(int, raw_input().strip().split(' '))
A = []
for _ in xrange(N) :
    A.append(map(int, raw_input().strip().split(' ')))
rowDic = {}
for r in map(int, raw_input().strip().split(' ')) :
    rowDic[r] = rowDic.get(r,0) + 1
colDic = {}
for c in map(int, raw_input().strip().split(' ')) :
    colDic[c] = colDic.get(c,0) + 1
 
for r in xrange(N) :
    x = rowDic.get(r+1,0)%N
    if x != 0 :
        tmp = A[r][:]
        for i in xrange(N) :
            A[r][i] = tmp[i-x]
 
 
for c in xrange(N) :
    x = colDic.get(c+1,0)%N
    if x != 0 :
        tmp = [A[i][c] for i in xrange(N)]
        for i in xrange(N) :
            A[i][c] = tmp[i-x]
 
for i in xrange(N) :
    print ' '.join(map(str,A[i]))
'''    
from collection import Counter as cnt
N, R, C = [int(x) for x in input().split()]
matrix  = [int(x) for x in input().split()]
if R:row_indx = Counter([int(x) for x in input().split()])
if C:col_indx = Counter([int(x) for x in input().split()])
for x in range(N):
    y = row_index[x][1] % N
    if y != 0:
        tmp = A[x]
