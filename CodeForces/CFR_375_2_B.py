lens = int(input())
ins = input()
p, t, c, m = 0, 0, 0, 0
for i in range(lens):
    if ins[i] == "_":
        if p and t: c += 1
        if not p and t>m: m = t
        t = 0
    elif ins[i] == "(":
        p = 1
        if t > m: m = t
        t = 0
    elif ins[i] == ")":
        p = 0
        if t: c += 1
        t = 0
    else:
        t += 1
if t > m : m = t
print(m, c)

