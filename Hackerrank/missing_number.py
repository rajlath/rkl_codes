'''
Sample Input

10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
Sample Output

204 205 206

'''
from collections import Counter
nos_a = int(input())
a = Counter([x for x in input().split()])
nos_b = int(input())
b = Counter([x for x in input().split()])
missing = set()
for bx in b.items():
    ch = bx[0]
    ci = bx[1]
    if ch in a:
        if a[ch] < ci:
            missing.add(ch)
print(" ".join(sorted(missing)))           

