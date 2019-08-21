_, amount = [int(x) for x in input().split()]
has = sorted(set([int(x) for x in input().split()]))
i = 1
need = []
while i <= amount:
    if i not in has:
        need.append(i)
        amount -= i
        
    i += 1
print(len(need))
print(*need)
