def encrypt(cleartext,key):
    ciphertext = ""
    key = key + cleartext
    i = 0
    while i < len(cleartext):
        ciphertext += __vig( cleartext[i], key[i] )
        i += 1
    return ciphertext

def decrypt(ciphertext,key):
    cleartext = ""
    i = 0
    while i < len(ciphertext):
        cleartext += __vig( ciphertext[i], key[i % len(key)], True )
        key += cleartext[-1]
        i += 1
    return cleartext

def __rot(l,d):
    # Rotate the letter l by the specified number of degrees (assume uppercase)
    return chr((((ord(l) - ord('A')) + d) % 26) + ord('A'))

def __vig(l,k,inverse=False):
    # Determine the index of key-letter 'k' relative to 'A' and use that
    # as the number of degrees to rotate by.
    degree = ord(k) - ord('A')
    if inverse:
        degree = -degree
    return __rot(l, degree)


print(encrypt("marywasnosyagain", "again"))