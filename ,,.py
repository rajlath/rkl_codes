
a, b, c, n = [int(x) for x in input().split()]
found = False
for i in range(1001):
    a1 = n - a * i
    if a1 < 0:break
    for j in range(1001):
        b1 = a1 - (b * j)
        if b1 < 0:break
        if b1 == 0:
            found = True
            x, y, z = i, j, 0
            break
        if c == 0:continue
        if b1 % c == 0:
            x, y, z = i, j, b1 // c
            found = True
            break
    if found:break
print(x, y, z)
'''
a,b,c,n=map(int,input().split())
st=False
for i in range(1001):
    lle=n-a*i

    if lle<0:
        break
    for j in range(1001):
        le=lle-b*j
        if le<0:
            break
        if le==0:
            st=True
            x=i
            y=j
            z=0
            break
        if c==0:
            continue
        if le%c==0:
            x=i
            y=j
            z=le//c

            st=True
            break
    if st:
        break
if x*a+y*b+z*c!=n:
    raise KeyError
print(x,y,z)
'''
