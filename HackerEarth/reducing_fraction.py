'''
SAMPLE INPUT
2
6 8
12 13
SAMPLE OUTPUT
3/4
12/13
'''
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer // common_divisor, denom // common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    #if reduced_den == 1:
    #    return reduced_num
    if common_divisor == 1:
        return str(numer)+"/"+str(denom)
    else:
        return str(reduced_num)+"/"+str(reduced_den)

for _ in range(int(input())):
    n, d = [int(x) for x in input().split()]
    print(simplify_fraction(n, d))