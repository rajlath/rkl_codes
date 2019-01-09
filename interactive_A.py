from sys import stdout
left, rite = 0, 1000000
while left != rite:
    mid = (left + rite + 1) // 2
    print(mid)
    stdout.flush()
    response = input()
    response = response.strip()
    if response == "<" :
        left = mid
    else:
        rite = mid - 1
print(left)
stdout.flush()
