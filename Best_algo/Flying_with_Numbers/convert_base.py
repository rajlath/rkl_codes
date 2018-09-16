def convert_to_decimal(number, base):
    '''
    convert a number string in base
    to decimal
    '''
    multiplier, result = 1, 0
    while number > 0:
        result += number%10 * multiplier
        multiplier *= base
        number //= 10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("Test Passed.")

def convert_from_decimal(number, base)    :
    multiplier, result = 1, 0
    while number > 0:
        result += number%base*multiplier
        multiplier *= 10
        number //= base
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("Test passed")

if __name__ == "__main__"    :
    test_convert_to_decimal()
    test_convert_from_decimal()


