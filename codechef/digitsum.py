def digit_sum(n):
    while n > 9 and n != 0:
        n = int(sum([int(x) for x in str(n)]))
    return n

def fill_dig_sum():
    ds = []
    for i in range(1, 10**5 + 5):
        ds.append(digit_sum(i))
    return ds
for _ in range(int(input())):
    m, n, x = [int(x) for x in input().split()]
    cnt = 0
    ds = fill_dig_sum()
    cnt = 0
    for i in range(m, n+1):
        #print(ds[i-1], i)
        cnt += ds[i-1] == x
    print(cnt)
