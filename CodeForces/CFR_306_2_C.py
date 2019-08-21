given = "00" + input()
l = len(given)
ans = "NO"
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            curr = given[i] + given[j] + given[k]
            curr = int(curr)
            if curr % 8 == 0:
                ans = "YES"
                print(ans)
                print(curr)
                break
        if ans == "YES"        :break
    if ans == "YES":break    
if ans == "NO":print(ans)
