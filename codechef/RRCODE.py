for _ in range(int(input())):
    n, k, answer = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    ops = input()
    if not k:print(answer)
    else:
        if ops == "XOR":
            if k % 2 == 0:
                pass
            else:
                for j in values:
                    answer ^= j
        elif ops == "AND":
            for j in values:
                answer &= j
        else:
            for j in values:
                answer |= j
    print(answer)           