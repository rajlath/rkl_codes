def update(bit, index, val, maxs):
    while index <= maxs:
        bit[index] += val
        index += index & -index

def query(bit, index):
    ans = 0
    while index > 0:
        ans += bit[index]
        index -= index & -index
    return ans

n = int(input())
arr = [int(x) for x in input().split()]
ans = 0
maxs = int(1e5)
bit1 = [0] * (maxs+1)
bit2 = [0] * (maxs+1)
bit3 = [0] * (maxs+1)

for i in range(n-1, -1, -1):
    ans1 = query(bit1, arr[i]-1)
    update(bit1,arr[i], 1, maxs )
    ans2 = query(bit2, arr[i] - 1)
    update(bit2, arr[i], ans1, maxs)
    ans3 = query(bit3, arr[i] - 1)
    update(bit3, arr[i], ans2, maxs);
    ans += ans3
print(ans)






