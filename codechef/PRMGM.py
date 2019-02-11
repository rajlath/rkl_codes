def is_prime(n):
    if n <= 1 : return False
    if n <= 3 : return True
    if not n % 2  or not n % 3 : return False
    i = 5
    while i * i <= n:
        if not n % i  or not n % (i + 2) :
            return False
        i += 6
    return True
nb_test = int(input())
for _ in range(nb_test):
    nb_elem = int(input())
    elems   = [int(x) for x in input().split()]
    alice = 0
    bob   = 0
    for i in range(nb_elem):
        curr = elems[i]
        prim = is_prime(curr)
        if not prim and not curr % 2:
            bob += 1
        elif not prim and curr % 2:
            alice += 1
    print(["Bob", "Alice"][alice >= bob])



