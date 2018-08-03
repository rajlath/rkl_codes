'''
2 5
2 3

6
'''
def days(mc, nod):
    curr = 0
    for machine in machines:
        curr += nod // machine
        if curr > int(10e12):
            return int(10e12)
    return curr

nom, goal = [int(x) for x in input().split()]
machines  = [int(x) for x in input().split()]
result = 0
lower  = 0
upper  = int(10e12)
while lower <= upper:
    mids = (lower + upper) // 2
    if days(machines, mids) >= goal:
        result = mids
        upper  = mids - 1
    else:
        lower  = mids + 1
print(result)

