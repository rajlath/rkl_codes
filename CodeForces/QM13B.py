from collections import Counter

ins = Counter(input())
ans =1
odd = 0
for _, v in ins.items():
    odd += v & 1
    if odd > 1:
        ans = 0
        break
print(ans)