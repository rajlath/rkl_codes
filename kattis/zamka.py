def dig_sum(n):
    return sum(int(x) for x in str(n))
l, d, x = [int(input())  for _ in range(3)]
for i in range(l, d+1):
    if dig_sum(i) == x:
        print(i)
        break
for i in range(d, l-1, -1):
    if dig_sum(i) == x:
        print(i)
        break
