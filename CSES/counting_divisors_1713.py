# Python3 program for finding
# number of divisor

# program for finding
# no. of divisors
def divCount(n):

    # sieve method for
    # prime calculation
    hh = [1] * (n + 1);
    p = 2;
    while((p * p) < n):
        if (hh[p] == 1):
            for i in range((p * 2), n, p):
                hh[i] = 0;
        p += 1;
    return hh

nb_test =int(input())
hh = divCount(10 ** 6 + 1)
for _ in range(nb_test):
    n = int(input())

    # Traversing through
    # all prime numbers

    total = 1;
    for p in range(2, n + 1):
        if (hh[p] == 1):
            # calculate number of divisor
            # with formula total div =
            # (p1+1) * (p2+1) *.....* (pn+1)
            # where n = (a1^p1)*(a2^p2)....
            # *(an^pn) ai being prime divisor
            # for n and pi are their respective
            # power in factorization
            count = 0;
            if (n % p == 0):
                while (n % p == 0):
                    n = int(n / p);
                    count += 1;
                total *= (count + 1);

    print(total)

