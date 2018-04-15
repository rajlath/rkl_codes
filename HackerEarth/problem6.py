from string import ascii_lowercase as lc
a, b = [x for x in input().split()]
cnts = 0
for x in lc:
    if x >= a and x <= b and x in 'aeiou':
        cnts += 1
print(cnts)
