from fractions import Fraction
for _ in range(int(input())):
    noe = int(input())
    ans = Fraction(1, 1)
    for i in range(noe):
        n, d = [int(x) for x in input().split()]
        ans =  ans * Fraction(n, d)
    print(ans.numerator, ans.denominator)