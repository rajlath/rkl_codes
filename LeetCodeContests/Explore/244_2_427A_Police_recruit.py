n = int(input())
r = [int(x) for x in input().split()]
sums = 0
miss= 0
for i in r:
    if sums <= 0 and i == -1:
        miss += 1
    else:
        sums += i
print(miss)