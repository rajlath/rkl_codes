n = input()
a = [int(x) for x in input().split()]
ai = [x for x in a if x != 0]
print(len(set(ai)))
'''
5 6 5 -4
0 1 0 -9
0 2 0 0
0 0 0 0
'''