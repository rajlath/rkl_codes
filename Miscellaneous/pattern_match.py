#Rabin-Karp Algorithm for string matching in O(|S| + |T|)

def match_pattern(s, t):
    '''
    given a string s and pattern t to match count all matches

    param string t : haystack
    param string s : needle
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

    #calculate the hash of the pattern t
    h_s = 0;
    for i in range(len(t)):
        h_s += (ord(t[i]) - 97) * p_pow[i]

    #iterate over all substrings of s having length |t| and compare
    #them with t
    i = 0
    while i + len(t) -1 < len(s):
        cur_h = hashes[i + len(t) - 1]
        if i: cur_h -= hashes[i-1]
        if cur_h == h_s * p_pow[i]:
            print(i, end=" ")
        i+= 1


match_pattern("rajkumarlathabcdefjlhjklhkohkhoionjkjhnkahnnfkndfsknk", "koh")
