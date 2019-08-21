has = input()
may = input()
ans = 0

def valid(cur):
    i = 0
    j = 0
    while i < len(cur) and j < len(may):
        if cur[i] == may[j]:
            j += 1
        i += 1
    return j == len(may)

for i in range(len(has) + 1):
    for j in range(i, len(has) + 1):
        curr = has[:i] + has[j:]
        if valid(curr):
            ans = max(ans, j - i)
print(ans)
