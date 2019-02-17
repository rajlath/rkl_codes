def is_armstrong(number):
    lens = len(str(number))
    return sum([int(i) ** lens for i in str(number)]) == number
