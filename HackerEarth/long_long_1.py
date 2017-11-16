#!/usr/bin/python
 
'''
# Read input from stdin and provide input before running code
 
name = raw_input()
print 'Hi, %s.' % name
'''
 
RI = lambda: map(int, raw_input().split())
 
A = 7648235
M = 15746361010203097
 
a = map(ord, raw_input())
n = len(a)
 
def check(k):
    t = set()
    p = pow(A, k, M)
    x = 0
    for i, y in enumerate(a):
        x = (x * A + y) % M
        if i - k >= 0:
            x -= a[i - k] * p % M
            if x < 0:
                x += M
        if i + 1 >= k:
            if x in t:
                return True
            t.add(x)
    return False
 
lo = 1
hi = n
while lo < hi:
    mid = (lo + hi + 1) / 2
    if check(mid):
        lo = mid
    else:
        hi = mid - 1
print lo
