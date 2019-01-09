from itertools import permutations

distances =     {}
places    =  set()

with open("input.txt") as f:
    for line in f:
        frm, _, to, _, amount = line.split(" ")
        distances[(frm, to)] = int(amount.strip())
        distances[(to, frm)] = int(amount.strip())
        places.add(frm)
        places.add(to)

valids = permutations(places)
totals = []
for route in valids:
    total = 0
    for i, place in enumerate(route):
        if i == len(route)-1:break
        total += distances[(place, route[i+1])]
    totals.append(total) 
print(min(totals), max(totals))    
         
            
        
    

        
        

