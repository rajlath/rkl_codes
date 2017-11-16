
input()
a=input()
b=input()
m=0
ans = [x for x in range(1,len(a)+1)]
for i in range(len(b)-len(a)+1):
    z=[]
    for j in range(len(a)):
        if a[j] != b[i+j]: z.append(j+1)
    if len(z)<len(ans):
        ans=z.copy()
print(len(ans))
print(*ans)
