from math import gcd
def count_set(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1
    return count
series = []


i = 1
while len(series) < 628000:
    sets = count_set(i)
    unse = len(bin(abs(i))[2:]) - sets
    if gcd(sets, unse) == 1:
        series.append(i)
    i += 1

nb_test = int(input())
for _ in range(nb_test):
    print(series[int(input()) - 1])
