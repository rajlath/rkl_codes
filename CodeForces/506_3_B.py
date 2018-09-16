noe = int(input())
arr = [int(x) for x in input().split()]
pos = 0
indx = 1
m = 0
for x in arr:
    if x > 2 * pos:
        m = 1
    else:
        m += 1
        indx = max(indx, m)
    pos = x
print(indx)