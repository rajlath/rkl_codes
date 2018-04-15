a,b=map(int,input().split())
F=[0,1]
for n in range(b):
  F.append(F[-1]+F[-2])
C=F[b-1]
l=(C//a)*a
print(l+a if(l+a-C)<(C-l)else l)  