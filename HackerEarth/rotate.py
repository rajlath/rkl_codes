s = "10"

def rotate(s, t, mode="right"):
    sl= len(s)
    d = [1,-1][mode=="left"]
    cnt = 0
    for x in range(t):
        t = [""]*sl
        for y in range(sl):            
            t[(y+d)%sl] = s[y]
        s = "".join(t)
        cnt += int(s,  2)%2==1    
        if t[0]==1:cnt += 1        
       
    return cnt        
    
for _ in range(int(input()))        :
    rotation = int(input())
    s = input()
    print(s.count("1"))
    
    
        
    
