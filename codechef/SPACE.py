def convert(b, d, r):
    val = []
    for i in  b:
        to_append = []
        for j in i:
            to_append.append(d[j])
        val.append(to_append)
    val.sort()
    print(val)
    ret = []
    for j in val:
        s = ''
        for k in j:
            s += r[k]
        ret.append(s)
    return ret

n = input()
a = input()
d ={}
r = {}
for i in range(26):
    d[a[i]] = i
    r[i] = a[i]
b = input().split()
show = convert(b, d, r)
print(' '.join(show))