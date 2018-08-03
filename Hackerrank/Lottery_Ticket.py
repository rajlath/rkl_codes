'''
5
129300455
5559948277
012334556
56789
123456879
'''
sums = [0] * 46


for i in range(int(input())):
    s = input()
    sk=sum([int(x) for x in set(s)])
    sums[sk]+= 1
cnt = 0
for i in range(46):
    if sums[45-i]:cnt += sums[45-i]
print(cnt)