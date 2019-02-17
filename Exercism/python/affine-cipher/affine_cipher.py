from string import ascii_lowercase as al
def encode(plain_text, a, b):
    encoded = ''
    for symbol in plain_text:
        if symbol in al:
            sym_index = al.find(symbol)
            encoded += al[(sym_index * a + b) % 26]
        else:
            encoded += symbol
    return encoded

print(encode('The quick brown fox jumps over the lazy dog', 17, 33))




def decode(ciphered_text, a, b):
    pass
