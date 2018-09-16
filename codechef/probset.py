'''
4
4 5
correct 11111
wrong 10101
correct 11111
wrong 01111
4 5
correct 10110
wrong 11111
correct 11111
wrong 01000
4 5
correct 11111
wrong 11111
wrong 10100
wrong 00000
4 5
wrong 10110
correct 01101
correct 11111
wrong 11000
'''
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    status = "FINE"
    for _ in range(n):
        a, b = [x for x in input().split()]
        zero = b.count("0")
        if a == "correct":
            if zero > 0:
                status = "INVALID"
        if a == "wrong":
            if zero == 0:
                if status == "FINE":
                    status = "WEAK"
                elif status != "WEAK":
                    status = "INVALID"
    print(status)