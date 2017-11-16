nos_of_elements = int(input())
arr = [int(x) for x in input().split()]
lens = nos_of_elements
ans = 0
while len(arr) > 0:
    if len(arr)==1:
        ans +=arr[0]
        
        break
    if len(arr)==2:
        ans += max(arr[0]+ arr[1], arr[0]*arr[1])
        
        break
    if len(arr)>=3:
        lst = [arr[0], arr[0]*arr[1], arr[-1], arr[-1]*arr[-2]]
        curr = max(lst)
        indx = [i for i, j in enumerate(lst) if j == curr]
        if len(indx)>1:
            if 3 in indx:   indx = 2
            if 1 in indx :  indx = 1
        else:indx = lst.index(curr)
        if indx == 0: arr = arr[1:][::-1]
        elif indx == 1:arr = arr[2:][::-1]
        elif indx == 2:arr = arr[:-1]
        else:arr = arr[:-2]
        ans += curr
    print(ans)    
print(ans)	
