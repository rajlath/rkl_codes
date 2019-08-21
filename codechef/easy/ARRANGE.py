for _ in range(int(input())):
    factor, msg = input().split()
    factor = int(factor)
    lens = 2 ** factor
    answ = [0] * lens
    for i in range(lens):
        answ[int((bin(i)[2:].zfill(factor)[::-1]), 2)] = msg[i]
    print("".join(answ))

