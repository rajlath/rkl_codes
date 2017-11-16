quality = [0] * 1005
qty= int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    quality[i] = 1
 
  
nos_girls = int(input())
matched = 0    
for _ in range(nos_girls):
    checked = []
    garr = [int(x) for x in input().split()]
    cnt = 0
    for j in garr:
        if quality[i]==1 and j not in checked:
            checked.append(j)
            cnt += 1
            if cnt == qty:
                break
    if cnt == qty:matched += 1
print(matched)    
                        
    

