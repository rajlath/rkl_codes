'''
http://codeforces.com/contest/1003/problem/B

Examples
input
2 2 1
output
1100
input
3 3 3
output
101100
input
5 3 6
output
01010100
'''
a, b, k = [int(x) for x in input().split()]
c = 1
if a >= b:c = 0
s = ''
while k > 1:
    s = s + str(c)
    if c == 1:b -= 1
    if c == 0:a -= 1
    c = 1 - c
    k -= 1

if c == 0:s = s + str(0) * a + str(1) * b
else: s = s + str(1) * b + str(0) * a
print(s)




