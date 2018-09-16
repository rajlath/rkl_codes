for _ in range(int(input())):
    eaten = int(input())
    n = 0
    count = 0
    i = 0
    while eaten > 0:
        n = 2 ** i
        if n > eaten:
            eaten -= (2 ** (i-1))
            count += 1
            i = 0
        elif n == eaten:
            eaten -= n
            count += 1
            break
        i += 1
    print(count)

