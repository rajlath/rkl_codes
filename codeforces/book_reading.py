nod, needed = [int(x) for x in input().split()]
worktime    = [int(x) for x in input().split()]
days = 0
for i in range(nod):
    needed -= (86400 - worktime[i])
    days += 1
    if needed <= 0:break
print(days)    
    
