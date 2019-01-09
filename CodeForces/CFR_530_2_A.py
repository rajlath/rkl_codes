R = lambda:[int(x) for x in input().split()]
w, h = R()
wa, ha = R()
wb, hb = R()
while h:
    w += h
    if ha == h:
        w = max(0, w - wa)
    if hb == h:
        w = max(0, w - wb)
    h -= 1
print(w)
