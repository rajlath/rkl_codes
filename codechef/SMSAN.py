'''
Input:
babe you're my life
Output:
1/2
'''


from fractions import Fraction
sms = [x for x in input().split()]
love = sum([1 for x in sms if x in ["love" ,"babe", "sweety", "life"]])
f = Fraction(love,len(sms))
if len(sms) != 0:
    print("{}/{}".format(f.numerator, f.denominator))
else:
    print("0/0")
