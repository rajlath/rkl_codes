'''
1
3
5
1
2
3
4
5
'''

m = int(input())
k = int(input())
piles = []
for _ in range(int(input())):
    piles.append(int(input()))
sums = [sum(piles[:m])]
left = 0
rite = left + m
while rite < len(piles):
    sums.append(sums[-1]-piles[left]+piles[rite])
    left +=1
    rite += 1
sums = sorted(sums, reverse=True)
print(sums)


