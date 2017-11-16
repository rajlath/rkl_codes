'''
SAMPLE INPUT 
2
3 3 5 4
3 1 1 2
8
0 1
2
1 1 1
2
0 1
2
1 2 4
2
SAMPLE OUTPUT 
NO
YES
NO
YES

'''
def binary_search(arr, val):
    low = 0
    high = len(arr) -1    
    while low < high:
        mid = (high + low) // 2        
        if arr[mid] > val:
            high = mid
        else:
            low  = mid + 1          
    if arr[low] >= val:
        return arr[low]
    return -1 
    
def generate_smallest(arr):
    stack = [arr[0]]
    for i in range(1, len(arr)):
        val = arr[i] 
        if val < stack[-1]:
            stack.append(val)
        else:
            stack.append(stack[-1]) 
    return stack
    
def get_ans(army, stack):
    if not stack:return "NO"
    elem = stack[-1]
    for i in range(1,len(army)):
        elem = binary_search(army[i], elem)        
        if elem == -1:return "NO"        
    return "YES" 
    
nos = int(input())
army = []
for _ in range(nos):
    row = [int(x) for x in input().split()]
    army.append(row[1:])    
stack = generate_smallest(army[0])


for _ in range(int(input())):
    print(army, stack)
    query = [int(x) for x in input().split()]
    cmd   = query[0]
    if cmd == 1:
        k, h = query[1:]
        army[k-1].append(h)
        if k == 0:
            if h < stack[-1]:
                stack.append(val)
            else:
                stack.append(stack[-1])
        print(army, stack)       
    elif cmd == 0:
        remov = query[1]
        army[remov-1].pop()
        if remov == 0:
            stack.pop()
        print(army, stack)    
    else:
        print(get_ans(army, stack))
                
        
                    
    
            
        


        
    
   
    
       
                
