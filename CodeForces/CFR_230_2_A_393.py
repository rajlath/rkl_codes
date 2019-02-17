from collections import Counter
nc = Counter("nineteen")
ins= Counter(input())

print(max(min([(ins['n'] - 1) // 2, ins['i'], ins['e'] // 3, ins['t']]), 0))