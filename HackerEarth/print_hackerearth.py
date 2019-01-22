from collections import Counter
nb = int(input())
s = Counter(input())
t = Counter("hackerearth")
ans = 100000000
for i in t:
    #print(i, t[i])
    if i in s:
        ans = min(ans, s[i]//t[i])
        print(ans)
    else:
        ans = 0
        break
print(ans)
