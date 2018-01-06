nos, mods = [int(x) for x in input().split()]
sums = 0
for i in range(1, nos+1):
    sums += i * 11
print(sums%mods)
