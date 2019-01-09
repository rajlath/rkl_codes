n, k = [int(x) for x in input().split()]
nums = [x for x in input().split()]
valid = 0
for x in nums:
    has = x.count("4") + x.count("7")
    valid += (has <= k)
   #print(has, valid)
print(valid)
