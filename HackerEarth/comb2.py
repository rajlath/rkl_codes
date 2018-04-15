n=input();r,c,a=xrange,[1]+[0]*n,[2,3,5]
for i in r(1,n+1):
    for j in r(3):
        if i>=a[j]:c[i]+=c[i-a[j]]
print c[n]
