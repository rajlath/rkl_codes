'''
3
ABAB
AABB
ABBA
'''
sums = 0
for _ in range(int(input())):
    s = [x for x in input()]
    t = []
    for a in s:
        if len(t)>0 and t[-1]==a:
            t.pop()
        else:
            t.append(a)
    if len(t)==0:sums +=1
print(sums)            

