def update_max(a, maxs):
    if a >= maxs[2]:
        maxs[0] = maxs[1]
        maxs[1] = maxs[2]
        maxs[2] = a
    elif a >= maxs[1]:
        maxs[0] = maxs[1]
        maxs[1] = a
    elif a >= maxs[0]:
        maxs[0] = a
    return maxs

def update_mins(a, mins):
    if a <= mins[0]:
        mins[1] = mins[0]
        mins[0] = a
    elif a < mins[1]:
        mins[1] = a
    return mins

def solution(A):
    mx = int(10e12)
    mn = int(-10e12)
    maxs = [mn, mn, mn]
    mins = [mx, mx]

    for i in A:
        maxs = update_max(i, maxs)
        mins = update_mins(i, mins)

    return max(maxs[0]*maxs[1]*maxs[2], mins[0]*mins[1]*maxs[2])

print(solution([-3,1,2,-2,5,6]))

