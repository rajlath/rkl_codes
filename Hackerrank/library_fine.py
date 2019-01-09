rd, rm, ry = [int(x) for x in input().split()]
dd, dm, dy = [int(x) for x in input().split()]

if ry > dy:
    ans = 10000
elif ry < dy:
    ans = 0
elif rm > dm:
    ans = (500 * abs(rm - dm))
elif rm < dm:
    ans = 0
elif rd > dd:
    ans = (15 *  abs(rd - dd))
else:
    ans = 0
print(ans)
