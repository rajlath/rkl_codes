q=int(input())
while(q):
    s=input()
    n=int(input())
    a=[]
    fl=1
    cn=0
    for i in range(len(s)):
        if s[i]=="0":
            a.append(i)
    l=len(a)
    if(n%2==0):
        m=n//2
    else:
        m=n//2+1

    ans=9999999999
    #print a
    print(l, m)
    for i in range(l-m+1):
        ans=min(ans,abs(a[i+m-1]-a[i]))
    print (ans)
    q-=1

'''
3
000111
4
0001
4
010
'''