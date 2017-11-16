
def find_trios(arr, M):
    arr = sorted(arr)
    lens= len(arr)
    cnt = 0
    for i in range(lens-2):
        for j in range(i+1, lens-1):
            for k in range(j+1, lens):
                if (arr[i]+arr[j]+arr[k])%M==0:
                    cnt += 1
    return cnt 
    
noe, M = [int(x) for x in input().split()]   
arr = [int(x) for x in input().split()]    
print(find_trios(arr, M))
    
                   
    
   
