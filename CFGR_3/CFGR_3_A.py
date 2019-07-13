# A. Another One Bites The Dust

a, b, c = [int(x) for x in input().split()]
print(c * 2 + min(a, b) + min(max(a, b), min(a,b) + 1))

