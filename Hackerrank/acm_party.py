from collections import Counter
for _ in range(int(input())):
    ans = "NO"
    s = list(Counter(input()).values())
    sums = sum(s)
    for i in s:
        if sums - i == i:
            ans = "YES"
            break
    print(ans)