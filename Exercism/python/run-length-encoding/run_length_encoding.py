from itertools import groupby
def decode(string):
    count = ''
    decoded = ''
    for i in string:
        if i.isdigit():
            count = count + i
        else:
            #print(count)
            if count == '':num = 1
            else:num = int(count)
            decoded += i * num
            count = ''
    return decoded

def encode(string):
    encoded = ''
    alls = []
    for k, g in groupby(string):
        alls.append((k, len(list(g))))
    for a, b in alls:
        if b == 1:
            encoded += a
        else:
            encoded += (str(b) + a)
    return encoded

from re import findall

def encode(text):
    """encode compresses text by replacing repeated characters
    with number of repeates and the character"""
    return ''.join(
        "%d%s" % (len(letters), letter) if len(letters) > 1 else letter
        for letters, letter in findall(r'((.)\2*)', text))

def decode(compressed):
    """decode uncompresses text but expanding repeated characters"""
    return ''.join(
        int(count) * letter if count else letter
        for count, letter in findall('(\d*)(.)', compressed ))



print(decode("2A3B4C"))
#print(encode(decode("b2a3c10z")))
print(encode('AABBBCCCC'))
