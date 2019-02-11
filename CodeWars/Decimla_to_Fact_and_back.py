
from math import factorial
from string import ascii_uppercase, digits

alpha = digits + ascii_uppercase

def max_fact(number):
    if number == 1:return 1
    indx = 1
    while number >  factorial(indx):
        indx += 1
    return indx - 1 if factorial(indx) > number else indx

#print(max_fact(463))

def decimal_to_string(number):
    max_factor = max_fact(number)
    out = ['0'] * (max_factor + 1)
    while number > 0:
        div, number = divmod(number, factorial(max_factor))
        out[max_factor] = alpha[div]
        max_factor = max_fact(number)
    return "".join(out[::-1])

def factorial_to_decimal(number):
    return sum([alpha.index(s)* factorial(i) for i, s in enumerate(number[::-1])])

print(decimal_to_string(463))
print(factorial_to_decimal(decimal_to_string(463)))
