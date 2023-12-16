with open("input.txt") as f:
    inps = f.read().splitlines()
 

verticals = list(("".join(x) for x in list(zip(*inps))))

grids = []
for row in verticals:
    row = row.split("#")
    row = sorted(row, reverse=True)
    row = "#".join(row)
    grids.append(row)


res = 0  
grids = list(map("".join, zip(*grids)))
lens = len(grids) 
for r, row in enumerate(grids):
    res += (row.count("O") * (lens - r))
print(res)    # res = 100170  106990
    
       

   
    
    

