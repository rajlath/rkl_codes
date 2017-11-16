from collections import Counter
input()
lst = Counter([int(x) for x in input().split()])
lst = lst.most_common()
maxs= lst[0][0]
maxc = lst[0][1]
for k, v in lst:
    if v == maxc:
        mx = max(maxs, k)
    else:
        break    
print(mx)        

