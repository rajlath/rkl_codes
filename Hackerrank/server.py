'''
5
1 2 3 4 5
1 1 1 1 1
'''

nos = int(input())
pos = [int(x) for x in input().split()]
hts = [int(x) for x in input().split()]

will_fallL = True
i = 0
while will_fallL or i >=nos:
    reach = pos[i] + hts[i]
    for j in range(i+1, nos):
        if pos[j] <= reach:
            continue
        else:break
    if j > i:
        i = j
    else:
        will_fallL = False
        break

will_fallR = True
i = nos - 1
while will_fallR or i <=0:
    reach = pos[i] - hts[i]
    for j in range(i-1,0):
        if pos[j] <= reach:
            continue
        else:break
    if j < i:
        i = j
    else:
        will_fallR = False
        break



if will_fallL and will_fallR:
    print("NONE")
elif will_fallL and not will_fallR:
    print("RIGHT")
elif not will_fallL and will_fallR:
    print("LEFT")
else:
    print("BOTH")












