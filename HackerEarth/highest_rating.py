def find_hightest(Q, arr, M):
    rankings = {}
    mini = min(arr)
    maxi = max(arr)
    left = 0
    rite = 0
    rank = 0
    
    for i in arr:
        if i !=mini:
            diff=i-mini
            t=diff//M
            if t<Q:
                mult=t*M
            else:
                mult=Q*M
            left = i-mult
        else:
            left=i
            if i !=maxi:diff1=maxi-i                
            t1=diff1//M
            if t1<Q:
                mult1=t1*M
            else:
                mult1=Q*M
            rite=i+mult1
        else:
            rite=i
            
        for j in range(left,rite+1,M):
            if j not in dic:
                dic[j]=1
            else:
                dic[j]=dic[j]+1 
     for i in rankings.values():
        if i > rank:
            rank=i
     return rank             
    
