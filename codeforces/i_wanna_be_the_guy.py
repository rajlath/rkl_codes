'''
4
3 1 2 3
2 2 4
'''
level = int(input())
if len(list(set(input().split()[1:]).union(set(input().split()[1:])))) == level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!") 
     
        
        
    
            
    


