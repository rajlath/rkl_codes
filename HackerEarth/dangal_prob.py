
l , t = [int(x) for x in input().split()]
arr = []
for i in range(l):arr.append(int(input()))

count = 0
for i in range(l)   :
    s = arr[i]
    if s <= t:
        count += 1
        j = i + 1
        while s <= t and j < l:
            s += arr[j]
            count += s <= t
            j += 1
total = (l * (l + 1) / 2) 
ans = count / total
print(ans)           

        
        
    
            
    
