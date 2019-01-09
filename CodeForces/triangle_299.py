nos = int(input())
seg = []
for _ in range(nos):
    seg.append(int(input()))
seg = sorted(seg)
#print(seg)
a, b, c = 0, 0, 0
found = False
for i in range(nos-2):
        a = seg[i]
        b = seg[i+1]
        c = seg[i+2]
        #print(a, b, c)
        if a + b > c:
            break
print(a, b, c)