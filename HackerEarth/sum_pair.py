'''
5 9
1 2 3 4 5
SAMPLE OUTPUT 
YES
'''

noe, needed = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
matches = []
ans = "NO"
for i in arr:
    if i in matches:
        ans = "YES"
        break
    else:
        matches.append(needed - i)  
print(ans)          
        
