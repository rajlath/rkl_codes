'''
find minimal integer : factorial of which contains
exactly given integer number of zeros.break
'''
def T0(n):
    r = 0
    while n:
        r += n //5
        n //= 5
    return r

def can(q):
    i = 0
    j = 1 << 31
    while i <= j:
        mid = (i + j) >> 1
        tmp = T0(mid)
        if tmp > q:
            j = mid - 1
        elif tmp < q:
            i = mid + 1
        else:
            while mid%5:
                mid -= 1
            return mid
    return 0

n = int(input())
t = can(n)
if T0(t) != n:
    print("No solution")
else:
    if t > 0:print(t)
    else:print(1)
