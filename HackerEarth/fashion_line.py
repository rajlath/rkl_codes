def is_special(s, t, i, k):
    for i in range(i,i+k):
        if s[i]  in t:
            return True
    return False        
            

for _ in range(int(input())):
    n, k, l, r = [int(x) for x in input().split()]
    dt = input()
    spl= input()
    specials = [0]*n
    for i in range(n):
        if is_special(dt, spl, i, k):specials[i]= "-"
        
    ans,cl,cr=0,0,0
    pl,pr = -1, -1
    
    for x in range(n):
        while pl < n   and cl < l:
            pl+=1
            if specials[pl] == "-": cl+=1
        while pr < n - 1 and cr < r:
            pr +=1
            if specials[pr] == "-" : cr += 1
        if specials[pr] =="-" and cr > r:
            pr -= 1
            cr -= 1
        if (l==0): ans+=pr-i+1
        else: ans+=pr-pl+1
        if specials[x] == "-":
            cl -= 1
            cr -= 1
        print(l)    
    print(ans)  
               
            
        
        
            
    
