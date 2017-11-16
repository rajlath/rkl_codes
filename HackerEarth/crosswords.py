x = [-1, -1, -1, 0, 0, 1, 1, 1]
y = [-1, 0, 1, -1, 1, -1, 0, 1]

def search_in_grid(grid, row, col, needle, R, C):
    wl = len(needle)
    for k in range(wl):
        lookfor = needle[k]
        matched = False                
        for d in range (8):
            rd = row + x[d]
            cd = col + y[d]
            if rd >= R or rd < 0 or cd >= C or cd < 0:
                continue
            if grid[rd][cd] == lookfor:
                matched = True
                break
    if k == wl -1:
        return True
    else:
        return False                

                
        
        

   
   
    wl = len(needle)
    for d in range(8):
        rd = row + x[d]
        cd = col + y[d]
        for k in range(1, wl):
            if rd >= R or rd < 0 or cd >= C or cd < 0:
                break
            if grid[rd][cd] != needle[k]:
                break
            #rd += x[d]
            #cd += y[d]
    if k == wl: return True
    else:return False 
    
def pattern_search(grid, word, R, C):
    for row in range(0, R):
        for col in range(0, C):
            if not grid[row][col] == word[0]:
                continue
            else:
                if search_in_grid(grid, row, col, word[1:], R, C) :
                    return True
                    
    return False 
    
                   
    
a = int(raw_input())
grid = []
for i in range(a):
    grid.append(raw_input().split()) 
    
allfound = True    
for j in range(int(raw_input()))    :
    curr = raw_input()
    if not pattern_search(grid, curr, a, a):
        allfound = False
        break
print(allfound)        
        
                
                
            
        
            





 
