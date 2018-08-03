'''
6 4
loves
doesnt
sincerely
doubts
'''

petals, nop = [int(x) for x in input().split()]
phrases = []
for _ in range(nop):
    phrases.append(input())
print(phrases[(petals % nop) - 1])
