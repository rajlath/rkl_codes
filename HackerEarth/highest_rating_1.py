#Copied
 def findHighestRating (Q, arr, M):
    #Q times
    dic={}
    #mult=Q*M
    maxi=arr[0]
    mini=arr[0]
    rank=0
    lowerbound=0
    upperbound=0
    for i in arr:
        if i<mini:
            mini=i
        if i>maxi:
            maxi=i
    for i in arr:
        if i !=mini:
            diff=i-mini
            t=diff//M
            if t<Q:
                mult=t*M
            else:
                mult=Q*M
            lowerbound=i-mult
        else:
            lowerbound=i
        if i !=maxi:
            diff1=maxi-i
            t1=diff1//M
            if t1<Q:
                mult1=t1*M
            else:
                mult1=Q*M
            upperbound=i+mult1
        else:
            upperbound=i
        for j in range(lowerbound,upperbound+1,M):
            if j not in dic:
                dic[j]=1
            else:
                dic[j]=dic[j]+1
                
    for i in dic.values():
        if i >rank:
            rank=i
    return rank        
 
M = int(input())
Q = int(input())
N = int(input())
#arr = map(int, input().split())
arr=[int(el) for el in input().split()]
out_ = findHighestRating(Q, arr, M)
print (out_) 
          
 
