'''
6 100
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR...
'''
rows, cols = [int(x) for x in input().split()]
grid = []
can = True
r=0
b=0
g=0
for i in range(rows):
    grid.append(list(input()))
for i in range(rows):
    if len(set(grid[i])) == 1:        
        if grid[i][0] =="R": r+=1
        if grid[i][0] =="B": b+=1
        if grid[i][0] =="G": g+=1
    else:
        can = False
        break
       
if can:
    if r != b or b != g:can=False  
     
if not can:
    can = True
    r=0
    b=0
    g=0
    for i in range(cols):
        cols = [rows[i] for rows in grid]        
        if len(set(cols)) == 1:
            if cols[0] == "R":   r+=1
            elif cols[0] == "G": g+=1
            elif cols[0] == "B": b+=1            
        else:
            can=False
            break
           
if can:
    if r != b or b != g:can=False                
print("YES" if can else "NO")             
            
    
