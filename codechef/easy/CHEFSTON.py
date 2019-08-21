
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    value = [int(x) for x in input().split()]
    print(max([k // x * y for x, y in zip(times, value)]))