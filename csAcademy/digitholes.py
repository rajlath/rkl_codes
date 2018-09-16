
def holes(x):
    hole = 0
    for y in x:
        if int(y) in [0, 6, 9]:hole += 1
        elif int(y) == 8:hole += 2
    return hole

l, r = [int(x) for x in input().split()]
max_hole = 0
ans      = l
for i in range(l, r+1):
    hole = sum([holes(x) for x in str(i)])
    if hole > max_hole:
        ans = i
        max_hole = hole
print(ans)




