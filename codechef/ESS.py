'''
5
1 1 0 0 1
'''
noe = int(input())
lst = [x for x in input().split()]
cnt = 0
for i in range(noe+1):
    for j in range(i,noe+1):
        curr = lst[i:j]
        if len(curr)>0:
            if curr[0]==curr[-1]:cnt += 1
print(cnt)
