for _ in range(int(input())):
    lens, k = [int(x) for x in input().split()]
    vals = [int(x) for x in input().split()]
    vals_xor = 0
    for i in vals:
        vals_xor ^= i
    print(vals_xor ^ k)