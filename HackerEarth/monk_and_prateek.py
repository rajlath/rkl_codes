'''
SAMPLE INPUT 
2
40 50
SAMPLE OUTPUT 
55 0
'''

def r3gz3n(n):
    ans = 0
    ans += int(n)
    ans ^= sum([int(x) for x in list(n)])
    return ans
    
all_val = {}
_ = input()
arr = [x for x in input().split()]
for i in arr:
    curr = r3gz3n(i)
    all_val[curr] = all_val.get(curr, 0) + 1
   
vals = set(all_val.values())

if len(vals)==1:
    print(max(all_val))
else:
    all_vals = sorted(all_val.items(), key=lambda x: (-x[1], x[0])) 
    print(all_vals)    
    print(all_vals[0][0])
     
    

   
    
