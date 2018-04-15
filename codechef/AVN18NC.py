for _ in range(int(input())):
    mode = int(input())
    if mode == 1:
        a, b, c = [int(x) for x in input().split()]
        msg = input()
        encode = []
        for i, v in enumerate(msg):
            o = ord(v)
            curr = ((a+b)*o + c) ^ (i+1)
            print(curr, end=" ")
        print()
    else:
        a, b, c, n = [int(x) for x in input().split()]
        decode = ''
        msg = [int(x) for x in input().split()]
        for i, v in enumerate(msg):
            curr = ((v^(i+1)) - c)//(a+b)
            decode += chr(curr)
        print(decode)



