n = int(input())
a = [int(x) for x in input().split()]
pows = [2**i for i in range(32)]
b = set(a)
possible = False
num = 1
ans = (a[0],)
for i in range(n):
   for j in pows:
     if num == 1 and a[i]+j in b:
        num = 2
        ans = (a[i],a[i]+j)
     if num < 3 and a[i]+j in b and a[i]+j*2 in b:
        num = 3
        ans = (a[i],a[i]+j,a[i]+j*2)
        possible = True
   if num==3: break

print( num)
for q in ans: print(q,end=" ")