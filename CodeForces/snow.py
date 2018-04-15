'''
input
5
30 25 20 15 10
9 10 12 4 13
output
9 20 35 11 25
'''
nos_days = int(input())
piles = [int(x) for x in input().split()]
temps = [int(x) for x in input().split()]
melted = temps[0]
remain = []
remain.append(piles[0] - temps[0])
print(melted, end= " ")
for i in range(1, nos_days):
    melted = 0
    remain.append(piles[i])
    if temps[i] > temps[i-1]:
        for x in range(len(remain)):
            if remain[i] == 0:
                continue
            else:
                if remain[x]>temps[i]:
                    melted += temps[i]
                    remain[x] -= temps[i]
                else:
                     remain[x] = 0
                     melted += remain[x]
    
    print(melted, end = " ")


