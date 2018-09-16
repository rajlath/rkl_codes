nod = int(input())
low = [int(x) for x in input().split()]
hii = [int(x) for x in input().split()]
clo = [int(x) for x in input().split()]
gapup = 0
gapdn = 0
for i in range(1, nod):
    if low[i] > clo[i-1]: gapup += 1
    if hii[i] < clo[i-1]: gapdn += 1
    
print(gapup, gapdn)
