lens, maxop, rowop = [int(x) for x in input().split()]
a, b = sorted([int(x) for x in input().split()], reverse=True)[:2]
times = maxop // (rowop + 1)
answer = times * a * rowop + times * b + (maxop - times * (rowop + 1)) * a
print(answer)
