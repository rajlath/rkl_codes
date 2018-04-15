sign = lambda x: x and (1, -1)[x < 0]

print(sign(-0))