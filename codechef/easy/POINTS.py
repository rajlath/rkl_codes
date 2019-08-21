def main():
    from sys import stdin,stdout
    from math import sqrt
    inp = stdin.readline
    out = stdout.write

    res = []
    def dist(x1,y1,x2,y2):
        return (sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))

    t = int(inp().strip())
    for _ in range(t):
        b=inp()
        n = int(inp().strip())
        l=[]
        for i in range(n):
            x,y=map(int,inp().strip().split())
            l.append([x,y])
        l.sort(key=lambda x:-x[1])
        l.sort(key=lambda x:x[0])
        s = 0.0
        for i in range(n-1):
            s+=dist(*l[i],*l[i+1])
        s = '{:.2f}'.format(s)
        res.append(s)

    for i in range(t):
        out(res[i]+'\n')

if __name__ == '__main__':
    main()