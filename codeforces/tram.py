'''
input
4
0 3
2 5
4 2
4 0
output
6
'''

present = 0
maxs = 0
for _ in range(int(input())):
    en, ex = [int(x) for x in input().split()]
    present = present + (ex - en)
    maxs = max(maxs, present)
print(maxs)    
