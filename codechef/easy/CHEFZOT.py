lens = int(input())
elem = [int(x) for x in input().split()]

curr_len = 0
maxs_len = 0
for i in range(lens):
    if elem[i] > 0:
        curr_len += 1
    elif elem[i] == 0:
        curr_len = 0
    maxs_len = max(maxs_len, curr_len)
print(maxs_len)            
