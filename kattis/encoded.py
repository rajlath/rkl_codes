def decoded(string):
    sqr = int(len(string) ** 0.5)
    msg = []
    for i in range(0, len(string), sqr):
        msg.append(string[i:i+sqr][::-1])
    msg = list(zip(*msg))
    ret = ''
    for i in range(sqr):
        ret += ''.join(msg[i])
    return ret

nb_Test = int(input())
for _ in range(nb_Test):
    print(decoded(input()))

