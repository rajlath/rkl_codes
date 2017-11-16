def multipication(a, b):
    cnt = 0
    ans = 0
    anss=[]
    while(b):
        if b%2:
            ans+= a<<cnt
            s = "(" + str(a)+"<<"+str(cnt) +")"
            anss.append(s)
        cnt+=1
        b//=2    
    return ans, anss
    
for _ in range(int(input()))       :
    a, b = [int(x) for x in input().split()]
    _,ans = multipication(a, b)
    print(" + ".join(ans[::-1]))
    
