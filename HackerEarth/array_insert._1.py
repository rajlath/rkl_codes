def prepare_array(arr):
    sums = [0] * len(arr)
    sums[0] = arr[0]
    for i in range(1,len(arr)):
        sums[i] = sums[i-1] + arr[i]
    return sums
    
def update_array(arr, pos, value):
    diff = value - arr[pos]
    for i in range(pos, len(arr)):
        arr[i]+= diff
    print(arr, diff)    
    return arr    
        
def get_sum(arr, start, end)        :
    return  arr[end]-arr[start-1]
    
noe, noq = [int(x) for x in input().split()]    
arr = [int(x) for x in input().split()] 
sums = prepare_array(arr)

for i in range(noq):
    a, b, c = [int(x) for x in input().split()] 
    if a == 1:
        arr[b] = c
        
    if a == 2:
        print(sum(arr[b:c+1]))    
        
        
        

