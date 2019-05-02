while True:
    try:
        a, b = [int(x) for x in input().split()]
        print(abs(a - b))
    except ValueError:
        break
    except EOFError:
        break
