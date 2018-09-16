from collections import Counter
lens = int(input())
s = input()
sc = Counter(s)
ans = "No"
if len(set(s)) == 1:
    ans = "Yes"
else:
    for i in sc:
        if sc[i] >=2:
            ans = "Yes"
            break
print(ans)
