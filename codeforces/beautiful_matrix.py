matrix = []
for i in range(5):
    s = input().split()    
    if "1" in s:
        r = i+1        
        c = s.index("1") + 1
        break
print(r, c)        
print(abs(r-3) + abs(c-3))        
