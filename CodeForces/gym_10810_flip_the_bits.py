for _ in range(int(input())):
    n = int(input())
    print(bin((n ^ (n - 1)))[2:].count("1"))