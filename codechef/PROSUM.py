for _ in range(int(input())):
    nb = int(input())
    c1, c2, c3 = [0] * 3
    arrs = [int(x) for x in input().split()]
    for i in arrs:
        c1 += i == 1
        c2 += i == 2
        c3 += i == 0
    nb -= (c1 - c3)
    answer = (nb * (nb - 1)) // 2
    answer -= (c2 * (c2 -1)) // 2
    print(answer)
                  