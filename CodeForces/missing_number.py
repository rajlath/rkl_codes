'''
3 5
0 2
2 4
3 5
'''

teleport_cnt, destination = [int(x) for x in input().split() ]
houses = set()
ans = "YES"
ports = []
for _ in range(teleport_cnt):
    a, b = [int(x) for x in input().split() ]
    ports.append((a, b))
    for i in range(a, b+1):
        houses.add(i)
house = list(houses)
sums = sum(house)
sum1 = (house[-1] * (house[-1] + 1)     )//2
print(sums, sum1, house)
if sums != sum1:
    print("NO")
else:
    print("Yes")







