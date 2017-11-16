n=int(input())
b=[0]*7
for j in range(n):
    a=list(input())
    for j in range(7):
        b[j]+=int(a[j])
print(b)
print (max(b))
