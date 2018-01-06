n, k = [int(x) for x in input().split()]
current_xor = 0
arr = range(1, n+1)
for i in range(k):
    current_xor  = current_xor ^ arr[i]
max_xor = current_xor

for i in range(k-1, n, 1):
    current_xor = current_xor ^ arr[i-k]
    current_xor = current_xor ^ arr[i]

    max_xor = max(max_xor, current_xor)


print(max_xor)