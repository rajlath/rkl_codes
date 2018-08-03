noc = int(input())
sps = input()
groups = []
curr = " "
cnt  = 0
for i in range(noc):
    if sps[i] == curr:
        cnt += 1
    else:
        cnt = 1
        groups.append((sps[i], cnt))
        curr = sps[i]
result = 0
for i in range(len(groups)):
    curr_len = groups[i][1]
    result += (curr_len * (curr_len + 1)) // 2
    if curr_len == 1 and i > 0 and (i+ 1) < len(groups) and (groups[i-1][0] == groups[i + 1][0]):
        result += min(groups[i-1][1],groups[i + 1][1])
print(result)


