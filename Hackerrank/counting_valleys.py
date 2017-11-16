'''
Sample Input

8
UDDDUDUU
Sample Output

1
'''

nops = int(input())
ops  = input()

level = 0
valley = 0
below_sea = False

for i in ops:
    if i == "U":
        level += 1
    else:
        level -= 1
    
    if not below_sea and level < 0:
        valley += 1
        below_sea = True
        
    if level >= 0: below_sea = False
    
print(valley)                
