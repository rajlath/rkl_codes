def append_at_begining(x, L):
    return [x] + [elem for elem in L]

def bit_string(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return append_at_begining("0", bit_string(n-1)) + append_at_begining("1", bit_string(n-1))

def bit_string_1(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    return [digit + bitstring for digit in bit_string_1(1) for bitstring in bit_string_1(n-1)]
print(bit_string_1(4))



