def compare_two_sub_string(s, l, i1, i2):
    '''
    compare two substring of string s  at index  i1 and i2 for length l
    param s string
    param lens int
    param i1 int
    param i2 int
    ret bool
    '''
    lens = len(s)
    p = 31
    p_pow = [0] * lens
    p_pow[0] = 1
    #calculate all powers of p
    for i in range(1, lens):
        p_pow[i] = p_pow[i-1] * p
    #calulate hash of all prefix
    hashes = [0] * lens
    for i in range(lens):
        hashes[i] = (ord(s[i]) - 97) * p_pow[i]
        if i : hashes[i] += hashes[i-1]

    #Get the hashes of two substrings
    h1 = hashes[i1 + l-1]
    if i1: h1 -= hashes[i1-1]
    h2 = hashes[i2 + l-1]
    if i2: h2 -= hashes[i2 - 1]

    #Get the two hashes multiplied by the same power of P and then compare them
    if (i1 <i2 and h1 * p_pow [i2-i1] == h2 or  i1> i2 and h1 == h2 * p_pow [i1-i2]):
        return True
    else:
        return False

print(compare_two_sub_string("rajkumakumalath", 4, 3,7)) #True
