def _push(arr):
    return arr[1:] + [arr[0]]
def _pop(arr)    :
    return arr[1:]

'''
3
3 2 1
1 3 2
''' 

noe = int(input())   
call_order = [int(x) for x in input().split()]
exec_order = [int(x) for x in input().split()]
exec_time  = 0
i = 0
while(len(call_order)!=0):
    if call_order[i] == exec_order[i]:
        call_order = _pop(call_order)   
        exec_order = _pop(exec_order)
        exec_time += 1
    else:
        call_order = _push(call_order)
        exec_time += 1
        if call_order == exec_order:
            exec_time += len(call_order)
            break
    #print(call_order)    
print(exec_time)    
        
    
    


    
            
        
        
        

    
