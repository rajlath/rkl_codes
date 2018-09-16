'''
D. Relatively Prime Graph

Examples
input
5 6
output
Possible
2 5
3 2
5 1
3 4
4 1
5 4
input
6 12
output
Impossible
'''
from math import gcd
from math import gcd

n, m = map(int, input().split())

a = []

if m < n-1:
    print("Impossible")
    exit()

for i in range(1, n):
    for j in range(i+1, n+1):
        if gcd(i, j) == 1:
            a.append([i, j])
        if len(a) == m:
            break
    if len(a) == m:
        break

if len(a) != m:
    print("Impossible")
    exit()

print("Possible")
for x in a:
    print(x[0], x[1])


