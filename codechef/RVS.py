'''
cats and dogs
'''

s = [x for x in input().split()]
for _ in range(len(s)):
    print(s.pop(), end=" ")