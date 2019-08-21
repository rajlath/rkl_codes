for _ in range(int(input())):
    lens = int(input())
    heard = [int(x) for x in input().split()]
    heard = [heard[0]] + heard + [heard[-1]]
    i = 1
    count = 0
    for i in range(1, lens + 1):
        if heard[i] != heard[i - 1] or heard[i] != heard[i + 1]:
            count += 1
    print(count)            