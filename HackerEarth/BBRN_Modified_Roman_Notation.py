from string import ascii_uppercase as uc
import math
romans = [1, 5]
for i in uc[2::2]:
    romans.append(romans[-2] * 10)
    romans.append(romans[-2] * 10)
def decimal2Roman(dec):
    if dec == 0:return ''
    digit = 0
    result=''
    rem  = dec
    dec_len = len(str(dec))
    while dec_len > 0:
        factor = 10 ** (dec_len - 1)
        digit  = rem // factor
        rem = rem - digit * factor
        

