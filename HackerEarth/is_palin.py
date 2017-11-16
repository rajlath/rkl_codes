for _  in range(int(input())):
    ne, nq = [int(x) for x in input().split()]
    s = input()
    a = [[0 for x in range(ne+1)] for y in range(27)]
  
    for i in range(1, ne+1):
        for j in range(26):
            a[j][i] = a[j][i-1]
            a[ord(s[i-1]) - 97][i]+=1
    for i in range(nq)       :
        l, r = [int(x) for x in input().split()]
        odd = 0
        for x in range(27):
            c=a[i][r]-a[i][l-1]
            if c%2==1:odd += 1
            if odd > 1:
                break
        print("NO" if odd>1 else "YES")            
                
            
        
    
    
        
        
        
           


