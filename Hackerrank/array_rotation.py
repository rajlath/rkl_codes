array = [1,2,3, 4, 5, 6]
x = ["-"] * len(array)
n = 2
for i, v in enumerate(array):
    x[(i+n)%len(array)] = v

print(x)
