for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    ar = sum([int(x) for x in str(a)]) % 3
    br = sum([int(x) for x in str(b)]) % 3
    print((ar * br)%3)