'''
Input
3000 1000 500
30 15 60

Output
8
'''
pm, rm, sm = [int(x) for x in input().split()]
m, r, s    = [int(x) for x in input().split()]

print(min(pm//m, rm//r, sm//s))