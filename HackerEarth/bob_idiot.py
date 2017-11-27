'''
1
W H
WelloHorld
'''
seen = {}
seen1 = {}
for _ in range(int(input())):
    a, b = [x for x in input().split()]
    if a not in seen and b not in seen:
        seen[a] = seen.get(a, b)
        seen[b] = seen.get(b, a)
    elif a  in seen and b in seen:
        seen[a], seen[b] = seen[b], seen[a]
    elif a not in seen and b in seen:
         seen[b] = seen[a]
         seen[a] = seen.get(a, b)
    elif a in seen and b not in seen:
        seen[a] = seen[a]
        seen[b] = seen.get(b, a)
    for k, v in seen.items():
        seen1[v] = k
        seen1[v+" "] = k + " "
    s = list(input())
    for i in range(len(s)):
        if s[i] in seen1:
            s[i]=seen1[s[i]]
    print("".join(s))








