'''
SAMPLE INPUT 
2 4
1 2 3 4

SAMPLE OUTPUT 
7
'''

k, n = [int(x) for x in raw_input().split()]
arr  = [int(x) for x in raw_input().split()]
maxs = 0
i, j = 0, n-1
x = k
for _ in range(x): 
    if sum(arr[:i+k]) > sum(arr[j-k:]):
        maxs += arr[i]
        i += 1
        k -= 1
    else:
        
        maxs += arr[j]
        j -= 1
        k -= 1     
        
print(maxs)        
            
