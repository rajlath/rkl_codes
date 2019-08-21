l11, l12, l21, l22, prink = [int(x) for x in input().split()]
begin = max(l11, l21)
ends  = min(l12, l22)
meeting = max(0, ends - begin + 1)
meeting += begin <= prink <= ends
print(meeting)
