'''
Examples
 input
2 0 0
1 2
2 3
 input
2
 input
2 1 0
1 2
2 2
 input
0
 input
2 5 7
3 4
14 4
 input
1
'''

n,k1,k2 = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
diffs = [abs(y-x) for x, y in zip(a, b)]
for _ in range(k1+k2+1):
    print(diffs)
    diffs[0] = abs(sorted(diffs,reverse=True)[0] - 1)


print(sum([a*a for a in diffs]))

