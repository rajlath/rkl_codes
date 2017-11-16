'''
5
1 1 1 3 3
'''

def is_denigerate(a, b, c):
    return (a + b) <= c or (a+c)<=b or (b+c)<=a
    
nos = int(input())    
peris = [int(x) for x in input().split()]
speris= sorted(peris, reverse=True)
printed = False
for i in range(nos-2):
    a, b, c = speris[i], speris[i+1], speris[i+2]
    if is_denigerate(a, b, c):
        print(c, b, a)
        printed = True
        break
if not printed:print(-1)        
        
        
    
    
