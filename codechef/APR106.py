n=int(input())
L=[]
for _ in range(n):
 L.append(int(input()))
def c(i):
 try:
     L[i]=L[i+1]-1;
 except:
     L[i]=L[i-1]+1;
 for k in range(n-1):
     if(abs(L[k]-L[k+1])>2):
         return 0
 return 1
f=0
for i in range(n):
 p=L[i]
 if(c(i)):
     f+=1
 L[i]=p
if(f>0):
 print("True")
else:
 print("False")

