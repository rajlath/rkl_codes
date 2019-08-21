while True:
    try:
        n = int(input())
        print(max(n // 2 + n // 3 + n // 4, n))
    except:
        break
