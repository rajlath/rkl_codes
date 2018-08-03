#solution passes small testcases
'''
from collections import OrderedDict
words = OrderedDict()
for i in range(int(input())):
    s = input()
    curr = []
    for indx, v in enumerate(s):
        curr.append([indx+1, v])
    words[i+1] = curr
for i in range(int(input())):
    l, r, pos, ch = [x for x in input().split()]
    l, r = int(l), int(r)
    need = [int(pos), ch]
    cnt = 0
    for x in range(l, r+1):
        if need in words[x]:
            cnt += 1
    print(cnt)
'''
#solution to avoid TLE
ch_cnt = [[[] for j in range(1000)] for i in range(1000)]
for i in range(int(input())):
    s = input()
    for j in range(len(s)):
        curr = ord(s[j]) - ord('a')
        ch_cnt[j][curr].append(i)
for i in range(int(input())):
    l, r, c, p = [x for x in input().split()]
    l, r, c    = int(l)-1, int(r), int(c)-1
    ch = ord(p) - ord('a')
    cnt= 0
    curr = ch_cnt[c][ch]
    #print(curr)
    for i in curr:
        if i >= l and i < r:
            cnt += 1
        else:
            break

    print(cnt)
'''
import sys

n = int(input())
arr = [[[] for col in range(1000)]for row in range(1000)]
for k in range(n):
    stri = input()
    for i in range(len(stri)):
        ch = int(ord(stri[i]) - ord('a'))
        arr[i][ch].append(k)
q = int(input())
for _ in range(q):
    l,r,c,p = input().strip().split(' ')
    l,r,c = [int(l) , int(r) , int(c)]
    l = l-1
    c = c-1
    ctr = 0
    k = ord(p) - ord('a')
    for i in arr[c][k]:
        if(i >= l):
            if(i < r):
                ctr += 1
            else:
                break
    print(ctr)
'''






