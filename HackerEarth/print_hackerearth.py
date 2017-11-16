from collections import Counter
s = Counter(input())
t = Counter("hackerearth")
alls = []
for i in s:
    if i in t:
        alls.append(s[i] // t[i])
    else:
        break    
print(min(alls))    
    
