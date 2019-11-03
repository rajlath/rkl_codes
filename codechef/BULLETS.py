for _ in range(int(input())):
    lens = int(input())
    pile = [int(x) for x in input().split()]
    xors = pile[0]
    for i in range(1, lens):xors ^= pile[i]
    print(["Isa","Gaitonde"][xors > 0])