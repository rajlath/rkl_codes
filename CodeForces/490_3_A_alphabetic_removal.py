from collections import Counter
n, k = [int(x) for x in input().split()]
s = input()
t = []
for i in range(len(s)):
    t.append([i, s[i]])
t.sort(key=lambda x:x[1])#this sort get char in sorted char order
t = t[k:]
#print(t)
t.sort() # this sort get char in original index order
ans = ''
for j in t:
    ans += j[1]
print(ans)





