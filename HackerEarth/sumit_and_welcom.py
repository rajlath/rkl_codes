'''
5
1 2 3 4 5
4 5 3 2 10
'''

input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [(a1+b1) for a1, b1 in zip(a, b)]
print(c)
