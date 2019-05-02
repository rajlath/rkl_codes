# cook your dish here
t=int(input())
for _ in range(t):
    n,d=map(int,input().split())

    a1=[]
    a2=[]
    while n>0:
        r=n%10
        a1.append(r)
        n=n//10
    a1.reverse()
    l=len(a1)
    m=min(a1)
    mp=a1.index(m)
    if m<=d:
        a2.append(m)
    else:
        a2.append(d)
    #print(MIN_pos)
    tmp=False
    i=mp+1

    while i < l:
        m=a1[i]
        for j in range(i+1,l):
            if m > a1[j]:
                m=a1[j]
                mp=j
                tmp=True
        if tmp:
            i=mp+1
            tmp=False
        else:
            i+=1
        if m<=d:
            a2.append(m)
        else:
            break
    a2 = a2 + (len(a1)-len(a2))*[d]
    a2 = list(map(str,a2))
    print(''.join(a2))