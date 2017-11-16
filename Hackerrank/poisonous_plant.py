'''
7
6 5 8 4 7 10 9
'''
n = int(input())
plants = [int(x) for x in input().split()]
days  = 0
while True:    
    stack = []
    stack.append(plants[0])
    lenp = len(plants)
    for i in range(1, lenp):
        if plants[i]< plants[i-1]:
            stack.append(plants[i])
    if lenp == len(stack):
        break
    else:
        days +=1
        plants = stack
print(days)                


        
    
    

