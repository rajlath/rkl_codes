#copied
for _ in range(int(raw_input())):
    n=int(raw_input())
    dist=map(int,raw_input().split())
    dist=sorted(dist)
    #print dist
    c=0;k=1;m=0
    for i in dist:
        if i<k:
            m=1;break
        else:
            c+=1
            k+=1
        if c%6==0:
            k+=1
    if m==1:
        print "Goodbye Rick"
        print c
    else:
        print "Rick now go and save Carl and Judas
