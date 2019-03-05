'''
nb_test = int(input())
for _ in range(nb_test):
    l, r, n1, n2 = [int(x) for x in input().split()]
    counts = [0] * 9
    begin  = l + 9 - l % 9
    ends   = r + 9 - r % 9
    #print(begin, ends)
    cycle  = ends - begin
    counts = [0] * 10
    for i in range(1, 10):
        counts[i] = cycle
    rs = l % 9
    re = r % 9
    for x in range(rs, re + 1):
        counts[x] += 1
    if counts[n1] == counts[n2]:
        print("Draw")
    elif counts[n1] > counts[n2]:
        print("Onkar")
    else:
        print("Krushna")
'''
def digsum(n):
    if n == 0:rets = 0
    else:
        rets = n % 9
        if not rets:rets = 9
    return rets

nb_test = int(input())
for _ in range(nb_test):
    l, r, n1, n2 = [int(x) for x in input().split()]
    counts = [0] * 10
    left = digsum(l)
    r -= l
    b = r % 9
    for i in range(b+1):
        if left + i <= 9:
            counts[left + i] = 1
        else:
            counts[(left + i) % 9] = 1

    if counts[n1] > counts[n2]: ans = "Onkar"
    elif counts[n2] > counts[n1]:ans = "Krushna"
    else:ans = "Draw"
    print(ans)









