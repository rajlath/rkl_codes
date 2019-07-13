nb_test = int(input())
for _ in range(nb_test):
    s = input()
    t = input()
    canbe = ''
    si = 0
    ti = 0
    while ti < len(t):
        if s[si] == t[ti]:
            canbe += t[si]
            si += 1
            ti += 1
        elif t[ti] == "+":
            canbe += "--"
            si += 2
            ti += 1
        else:
            canbe += t[ti]
            si += 1
            ti += 1
        if si >= len(s): break

    if canbe == s:print("YES")
    else:print("NO")



