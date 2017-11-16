
def rotate(arr, n):    
    s = arr[-1]    
    for i in range(n-1):
        s += arr[i]      
    return s
    
for _ in range(int(input()))    :
    slen = int(input())
    s  = input()
    cnt = 0
    for i in range(slen):
        s = rotate(s, slen)
        cnt += s[0]=="0"
    print(cnt)    
    

      
        
    

   

