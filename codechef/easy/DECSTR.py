for _ in range(int(input())):
    pos = int(input())
    lens, rems = divmod(pos, 25)
    rems += 97
    if rems != 97:
        while rems >= 97:
            print(chr(rems), end="")
            rems -= 1
    while lens > 0:
        for num in range(122, 98, -1):
            print(chr(num))
        lens -= 1
    print()                
