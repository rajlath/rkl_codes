'''
7 10
2 1 2 2 1 1
1 3 2 2 2 3
1 2 4 8 16 32
1 10 2 9 3 8 4 7 5 6
-1
0
26
0
26
16
26
16
24
24
'''

n, m = [int(x) for x in input().split()]
needed = [int(x) for x in input().split()]
replacement = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]
query = [int(x) for x in input().split()]


for i in range(m):
    expense = 0  
    possible = True  
    capacity = query[i]
    have = capacity
    for j in range(n-1):        
        needs = needed[j]
        print(have, needs)
        if have < needs:
            print(have, needs, replacement[j])
            if replacement[j] <= needs:
                possible = False
                break
            else:
                have = replacement[j]    
                expense += cost[j]
        else:
            have -= needed[j] 
            if have == 0:
                have = replacement[j]
                expense += cost[j] 
            print(have, expense)          
                
             
    print(possible)    
    print(expense if possible else "-1")            
            
                
            
        
        
    

