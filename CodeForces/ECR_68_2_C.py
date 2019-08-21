from collections import defaultdict
for _ in range(int(input())):
    s = list(input())
    t = list(input())
    p = list(input())
    cnt = defaultdict(int)
    for c in p:
        cnt[c] += 1
    pos = 0
    ans = "NO"
    for c in t:
        if pos >= len(s) or c != s[pos]:
            cnt[c] -= 1
            if cnt[c] < 0:
                ans = "NO"
                break
        else:
            pos += 1
    if ans != "NO" and pos >= len(s):
        print("YES")
    else:
        print("NO")
