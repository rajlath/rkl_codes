inp  = input()
if len(inp) %2 == 0:
    mid = len(inp)//2 - 1
else:
    mid = len(inp) // 2
left = mid
rite = mid
decoded = inp[mid]
while left > 0 and rite < len(inp):
    left -= 1
    rite += 1
    decoded +=  inp[rite] + inp[left]
if len(decoded) != len(inp):
    decoded += inp[-1]
print(decoded)
