from collections import defaultdict
def hash_for_string(s):
    '''
    calculating the hash of a string ss, which contains only lowercase letters
    for lowercase prime contsant 31
    for letters   prime constant 53
    param: s : string
    return int
    '''
    p = 31 # 53 in case of mixed case
    hash = 0
    p_pow = 1
    for i in range(len(s)):
        hash += (ord(s[i]) - 96 + 1) *  p_pow # + 1 is needed for a to be 1 96 ordinal of a
        p_pow *= p
    return hash
'''
Problem: Given a list of strings S[1..N],
each no longer than M characters, find all the duplicate strings and
divide them into groups so that each group contains only the same string.
'''
def fill_p_pows(lens=10000):
       '''
       Calculate all powers of p up to 10,000 or upto length of string
       lens: default 10000 or len of the string
       ret : array containing p_pows
       '''
       p = 31

       p_pow = [1] * lens
       for i in range(1, lens):
           p_pow[i] = p_pow[i -1] * p

       return p_pow

def find_duplicates(s):
        '''
        param array of string
        ret array of string
        '''
        p_pow = fill_p_pows(10)
        hashes = defaultdict(list)
        hash = 0
        allgrp = defaultdict(list)
        for i in range(len(s)):
            hash = 0
            for j in range(len(s[i])):
                hash += (ord(s[i][j]) - 97) * p_pow [j]
            allgrp[hash].append(i)
        groups = []
        for i, v in allgrp.items():
            groups.append(s[v[0]])
        return groups

print(hash_for_string("oorjahalt"))  #18270410632939
print(hash_for_string("raj"))        #10652
print(find_duplicates(["raj","kumar", "lath", "raj", "kumar"]))