n = int(input())
ans = (pow((1 + int(5 ** 0.5)), n) - pow((1 - int(5 ** 0.5)), n))
ans = ans // (pow(2, n) * int(5 ** 0.5))
print(ans)