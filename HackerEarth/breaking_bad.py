'''
2
3
Ram 100,000
Shyam 0.05
Sita 1000,549,001.10
Raman 2,007,900
Chaman 3,000
Gaman 1,990,678
'''

i=int(input());j=int(input())
for _ in range(i):
    maxs=("",0)
    for _ in range(j):
        a,b=input().split()
        comma=b.count(",")
    if comma==maxs[1] and a > maxs[0] or comma > maxs[1]:maxs :maxs=(a,comma)
    print(maxs[0], maxs[1])





