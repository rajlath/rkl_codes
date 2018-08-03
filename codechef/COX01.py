
digs = "0123456789"
alph = "ABCDEFGHIJ"
done = []
multi=  10
s = input().strip()
res = 1
if s[0] not in digs:
    res *= 9
if s[0] in alph:
    done.append(s[0])
    multi -= 1
for x in s[1:]:
    if x not in digs:
        if x == "?":
            res *= multi
        else:
            if x not in done:
                res *= multi
                done.append(x)


print(res)+

s = input()
l = len(s)
letters = "ABCDEFGHIJ"
used = []
ans = 1
val = 10
for i in range(l):
    #print(s[i],ans, i)
    if s[i] == '?' and i == 0:
        ans *= 9
    elif s[i] == '?':
        ans *= 10
    elif s[i] in letters and i == 0:
        ans *= 9
        used.append(s[i])
        val -= 1
    elif s[i] in letters and i != 0:
        if s[i] not in used:
            used.append(s[i])
            ans *= val
            val -= 1
print(ans)



