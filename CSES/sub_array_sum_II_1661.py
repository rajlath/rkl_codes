from collections import defaultdict
lens = int(input())
B = [0] * (lens + 1)
elements = [int(x) for x in input().split()]
B[0] += 1
curr_sums = 0
for i in range(lens - 1):
    curr_sums = (curr_sums + elements[i]) % lens
    B[curr_sums] += 1
ans = 0
for i in range(lens - 1):
    ans = ans + (B[i] * (B[i] - 1)) // 2
print(ans)

