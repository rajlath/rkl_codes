n = int(input())
rects = []
for i in range(n):
    rects.append([int(x) for x in input().split()])
max_height = max(rects[0])
for i in range(1, n):
    if max(rects[i]) <= max_height:max_height = max(rects[i])
    elif min(rects[i]) <= max_height:max_height = min(rects[i])
    else:max_height = 0
print("NO" if max_height==0 else "YES")












