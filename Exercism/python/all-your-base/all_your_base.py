def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("Invalid input base: {}".format(input_base))
    value = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("{} Not a valid digit for base {}".format(digit, input_base))
        value = value * input_base + digit

    digits = []
    if output_base < 2:
        raise ValueError("Invalid output base : {}".format(output_base))
    while value > 0:
        digits.insert(0, value % output_base)
        value //= output_base
    return digits

#print(rebase(16, [2, 10], 3))


