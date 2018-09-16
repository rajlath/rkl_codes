for _ in range(int(input())):
    n = int(input())
    x = 1
    while True:
        curr =  ((x) * (x+1))//2
        if curr == n:
            print()
            x += 1


