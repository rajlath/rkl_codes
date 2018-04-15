'''
2
abaabaabaaba 4
aaaaa 2
'''
for i in range(int(input())):
    sk = [x for x in input().split()]
    s = sk[0]
    if len(sk) == 2:
        k = int(sk[1])
    else: k = int(input())
    lens = len(s)
    ans = "YES"
    part = lens // k
    if part * k != lens:
        ans = "NO"
    else:
        for i in range(0, lens, part):
            curr = s[i:i+part]

            if curr != curr[::-1]:
                ans = "NO"
                break
    print(ans)

