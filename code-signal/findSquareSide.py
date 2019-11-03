
def findSquareSide(x, y):
    s=lambda x:x*x
    d=lambda a, b:s(a[0] - b[0]) + s(a[1] - b[1])
    a=d([x[0],y[0]],[x[1],y[1]])
    for i in range(2,4):
        a=max(a, d([x[i - 1], y[i - 1]], [x[i], y[i]]))
    if a > 2: return a
    return a//2


print(findSquareSide([0,1,0,1],[0,1,1,0]))
