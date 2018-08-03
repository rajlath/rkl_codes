'''
Examples
inputCopy
5 3
15 13 15 15 12
outputCopy
YES
1 2 5
inputCopy
5 4
15 13 15 15 12
outputCopy
NO
inputCopy
4 4
20 10 40 30
outputCopy
YES
1 2 3 4
'''
nos, grp = [int(x) for x in input().split()]
ratings  = [int(x) for x in input().split()]
ans = "NO"
if len(set(ratings)) >= grp:
    in_group=[]
    grp_index=[]
    for i in range(nos):
        if ratings[i] not in in_group:
            grp_index.append(i+1)
            in_group.append(ratings[i])
            if len(grp_index)>=grp:
                break
    if len(grp_index)>=grp:
        ans = "YES"
print(ans)
if ans == "YES":
    print(*grp_index)


