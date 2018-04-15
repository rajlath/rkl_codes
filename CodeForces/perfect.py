import math
def is_perfect(n):
    if n < 0: return False
    nsqrt = math.sqrt(n)
    return nsqrt == math.trunc(nsqrt)


noe = int(input())
arr = [int(x) for x in input().split()]
nots = []
for i in arr:
    if is_perfect(i):
        continue
    else:
        nots.append(i)
print(max(nots))



