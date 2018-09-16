from collections import Counter
for _ in range(int(input())):
    s1,s2 = [x for x in input().split()]
    s1c = Counter(s1)
    s2c = Counter(s2)
    ans = "Yes"
    for i in s1c:
        if i in s2c:
            if s2c[i] < s1c[i]:
                ans = "No"
                break
        else:
            ans = "No"                  
            break
    print(ans)
