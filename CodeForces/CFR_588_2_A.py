abcd = sorted([int(x) for x in input().split()], reverse=True)
need = 0
for x in abcd:
    if need <= 0:
        need += x
    else:
        need -= x
print(["No", "Yes"][need == 0])
