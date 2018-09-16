from collections import defaultdict
def digit_sum(n):
    sums = 0
    while n > 0 or sums > 9:
        if n == 0:
            n = sums
            sums= 0
        n, r = divmod(n, 10)
        sums += r
    return sums

limit = 10 ** 5 + 5
cnts = {x:[] for x in range(limit)}
count= [0 for x in range(10)]
for i in range(1, 20):
    curr = digit_sum(i)
    count[curr] += 1
    cnts[i] = count
print(cnts[2], cnts[11])
for _ in range(int(input()))    :
    m, n, x = [int(x) for x in input().split()]





