for _ in range(int(input())):
    a, b = input(), input()
    x = b[::-1].index("1")
    y = a[::-1].index("1", x)
    print(y - x)
