# syntatic translation of solution submitted by
# Preet Shah (Psp98) 
# From Java8 to Python3

noe, noq = [int(x) for x in input().split()]

query    =  []
max_left =  [0] * (noe + 2)
max_right=  [0] * (noe + 2)

arr      =  [0] * (noe + 2) # 1-index based array

for i  in range(noq):
    
    l, r, val   = [int(x) for x in input().split()]    
    query.append([l, r, val])               # store the query   
    arr[l] += val;                  # increment at position 'l' by val      
    arr[r + 1] -= val             # decrement at position 'r + 1' by val
    
    
    
    
        
for i in range(1, noe+1):
    arr[i] += arr[i-1]
    
#calculate prefix-max

for i in range(1, noe+1):
    max_left[i] = max(max_left[i - 1], arr[i])
         
#calculate suffix-max

for i in range(noe, i>=noe, -1):
    max_right[i] = max(max_right[i + 1], arr[i])
    
         
max_val = max_left[noe]      #Maximum value of the array after performing all queries
min_ans = max_val
    
for i in range(noq):
    l   = int(query[i][0])       # get the ith query 
    r   = int(query[i][1])
    val = query[i][2]
    
    #what if we ignore this query
    max1 = max_left[l - 1]      # maximum from 1 to (l - 1)
    max2 = max_val - val        # maximum from l to r
    max3 = max_right[r + 1]     # maximum from (r + 1) to n  
         
       
    max_current = max(max1, max(max2, max3))
    min_ans     = min(min_ans, max_current) #check if it is less than current minimum 
         
print(min_ans)                
 
    





 





