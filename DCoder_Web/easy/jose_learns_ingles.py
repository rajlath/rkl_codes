def func(x):
    return x.lower()

lens = int(input())
chrs = [x for x in input().split()]
answ = sorted(chrs, key= func)
print(*answ)

