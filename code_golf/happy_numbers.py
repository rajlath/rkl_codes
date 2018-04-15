
for i in range(1,200):
    x,j=[],i
    while i>1:
        i=sum(int(a)*int(a) for a in str(i))
        if i in x:break
        x.append(i)
    if i==1:print(j)

