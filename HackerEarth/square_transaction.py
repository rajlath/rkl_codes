n = int(input())
arr = [int(x) for x in input().split()]

trans_sum = [0] * (n+10)

trans_sum[0] = arr[0]

for i in range(1, n):
    amt  = trans_sum[i-1] + arr[i]
    trans_sum[i] = amt   
    
for i in range(int(input()))    :
    needed = int(input())
    for j in range()
