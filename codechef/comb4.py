h, w, x, y = [int(x) for x in input().split()]
area1 = 0
area2 = 0
if h%x == 0:
    w1 = (h // x) * y
    h1 = h
    if w1 <= w:
        area1 = h1 * w1
if w%y == 0:
    h2 = (w // y) * x
    w2 = w
    if h2 <= h:
        area2 = h2 * w2
#print(area1, area2)
if area1 == 0 and area2 == 0:
    print(0, 0)
elif area1 >= area2 :
    print(h1, w1)
elif area2 <= area1 :
    print(h2, w2)
else:
    print(0, 0)


