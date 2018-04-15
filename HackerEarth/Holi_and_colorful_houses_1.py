def process2(h):
    n = len(h)

    m = 0
    x = []
    for i in range(n):
        if h[i] != h[i-1]:
            m+=1
        if i == 0:
            x.append(0)
        elif h[i]==h[i-1]:
            x.append(x[-1])
        else:
            x.append(x[-1] + 1)

    return x,m


def main():
    t = int(input())
    for i in range(t):
        work2()


def work2():
    n, q = map(int, input().split())
    h = input()
    x,m = process2(h)
    print(x, m)
    for i in range(q):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        if b<=a:
            a,b = b,a
        op1 = (x[b]-x[a])
        op2 = m - op1
        print(min(op1, op2))


if __name__ == '__main__':
    main()