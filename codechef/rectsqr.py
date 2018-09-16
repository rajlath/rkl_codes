nots = int(input())
for _ in range(nots):
    a, b = [int(x) for x in input().split()]
    squares = 0
    mults = 1
    while a > 0 and b > 0:
        squares += (a * b * mults * mults)
        a -= 1
        b -= 1
        mults += 1
        #print (squares)
    print(squares)

