l = 1
r = 1000000
while l != r:
    mid = (l + r) // 2
    print(mid)
    resp = input()
    if resp == "<":
        r = mid - 1
    else:
        l = mid
print("! {}".format(l))        