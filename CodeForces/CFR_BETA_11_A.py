n, d = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
needed  = 0
for i in range(1, n):
    if numbers[i] <= numbers[i-1]:
        need_now = (numbers[i-1] - numbers[i]) // d + 1
        needed += need_now
        numbers[i] += d * need_now
print(needed)

