def P(n):
    if n<=1:return False
    for i in range(2,int(pow(n,0.5)+1)):
        if  n%i==0:return False
    return True
l,r=map(int,input().split());k=-1
for i in range(l,r+1):
    if P(i) and str(i)==str(i)[::-1]:
        k=i;break
print(k)


