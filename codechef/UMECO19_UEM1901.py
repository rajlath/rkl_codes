def remove_a_digit(n, d):
    rets = ''
    for i, v in enumerate(n):
        if v == d:continue
        rets += v
    return int(rets)


nb_test = int(input())
for _ in range(nb_test):
    ans = "Try again"
    a, b, d = [x for x in input().split()]
    c = str(int(a) + int(b))
    a = remove_a_digit(a, d)
    b = remove_a_digit(b, d)

    c = remove_a_digit(c, d)
    if a + b == c:
        print("Go ahead")
    else:
        print("Try Again")






