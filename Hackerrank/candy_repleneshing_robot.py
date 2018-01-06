'''
8 4
3 1 7 5
'''
current, times = [int(x) for x in input().split()]
withdrawl      = [int(x) for x in input().split()]
opbal = current
added = 0
for i in range(times):
    current -= withdrawl[i]
    print(current)
    if i != times-1:
        if current < 5:
            deposit = opbal - current
            added += deposit
            current+= deposit

print(added)


