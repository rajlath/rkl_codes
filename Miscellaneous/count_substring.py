#Determine the number of different substrings in a string

def count_substrings(s):
    '''
    count all unique substring in string s
    param string
    ret int
    '''
    lens = len(s)

    p = 31
    p_pow = [0] * lens
    p_pow[0] = 1
    #calculate all powers of p
    for i in range(1, lens):
        p_pow[i] = p_pow[i-1] * p

    #calculate hashes of all prefixes
    hashes = [0] * lens
    result = 0
    for i in range(lens):
        hashes[i] = (ord(s[i]) - 97) * p_pow[i]
        if i : hashes[i] += hashes[i-1]
    for i in range(1, lens):
        hs = set()
        for j in range(lens-i):
             cur_h = hashes[j + i-1]
             if j: cur_h -= hashes[i-1]
             cur_h *= p_pow[lens - i -1]
             hs.add(cur_h)
        result += len(hs)
    return result

print(count_substrings("rajkumarlath"))


