'''
Examples
input
5 1 1
*...*
output
2
input
6 2 3
*...*.
output
4
input
11 3 10
.*....**.*.
output
7
input
3 2 3
***
output
0
'''

R = lambda: map(int, input().split())

n, a, b = R()
ls = tuple(map(len, input().split('*')))

s = a + b
for t in ls:
    if t % 2:
        if a > b: a -= 1
        else: b -= 1
        t -= 1
    a -= t/2; b -= t/2

print(int(s - max(0,a) - max(0,b)))



