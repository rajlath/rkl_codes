'''
7 6
4 3 7 6 7 2 2
8 4
3 3 3 3 3 3 3 3
'''

noe, can_do = [int(x) for x in input().split()]
marks  = [int(x) for x in input().split()]
max_till_now = 0
max_done = 0
can_skip = True
for i in range(noe):    
    if marks[i]<=can_do:
        max_till_now += 1 
        max_done = max(max_done, max_till_now)       
    else:
        if can_skip:         
            can_skip = False
        else:
            break
            
           
print(max_done)                    
        
    

