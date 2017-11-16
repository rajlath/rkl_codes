from collections import defaultdict
noe = int(input())
arr = [int(x) for x in input().split()]
arrd = defaultdict(list)
maxl = -1
for i, v in enumerate(arr):
    #print(arrd)
    if v in arrd:
        arrd[v][1] =  i
        print(arrd[v])
        arrd[v][2] = arrd[v][1] - arrd[v][0]
        maxl = max(maxl, arrd[v][2])
    else:
        arrd[v].append(i)
        arrd[v].append(i) 
        arrd[v].append(1)
print(maxl+1)        
           
