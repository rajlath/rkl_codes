'''
SAMPLE INPUT 
5
1 -1 2 3 -2
SAMPLE OUTPUT 
2
'''
nos = int(input())
arr = [int(x) for x in input().split()]
stack = []
result = 0
tmp = 0
for i, v in enumerate(arr):
    if v > 0:
        if stack:
            tmp = 0
        stack.append(v)  
    else:
        if i != 0 and stack:
            if v == -1 * stack[-1]:
                stack.pop()
                tmp += 2
                result = max(result, tmp)
            else:
                stack = []
print(result)           
                
                
        
        


