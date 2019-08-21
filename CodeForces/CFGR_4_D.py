def lcs_(X, Y) :       
    m = len(X) 
    n = len(Y)  
  
    L = [[0] * (n + 1)] * (m + 1)
    for i in range(n + 1) :
        for j in range(n + 1) :
            if (i == 0 or j == 0) : 
                L[i][j] = 0;  
            elif (X[i - 1] == Y[j - 1]) : 
                L[i][j] = L[i - 1][j - 1] + 1
            else : 
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
      
    
    index = L[m][n]
    print(index)
  
    lcs = ["\n "] * (index + 1) 
  
    
    i, j= m, n  
    found = False  
    while (i > 0 and j > 0) :
      
        
        if X[i - 1] == Y[j - 1] and j - i >= len(X)/2 :
          
            found = True 
            lcs[index - 1] = X[i - 1] 
            i -= 1
            j -= 1
  
            
            index -= 1
          
        
        elif(L[i - 1][j] > L[i][j - 1]) : 
            i -= 1
              
        else : 
            j -= 1
      
    ans = "" 
    if not found:
        return "IMPOSSIBLE"
    else:
        for x in range(len(lcs)) : 
            ans += lcs[x] 
          
        return ans 
  

def longestPalSubseq(string) : 
    rev = string[: : -1]
    return lcs_(string, rev)


print(longestPalSubseq(input()))