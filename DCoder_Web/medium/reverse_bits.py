for _ in range(int(input())):
    ins = int(input())
    bins = bin(ins)[2:]
    bins = bins[::-1]
    print(int(bins, 2))