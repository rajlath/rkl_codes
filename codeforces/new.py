maxt = 0
days = []
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    for i in range(b+1):
        if (a+i) not in days:
            days.append(a+i)
print(max(days))            
