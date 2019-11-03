import re
from itertools import permutations

def find_min(s):
    freq = {ch:0 for ch in 'ATGC'}
    for ch in s:
        freq[ch] += 1
    desired_len = int(len(s)/4)
    fixes = {ch:desired_len-freq[ch] for ch in 'ATGC'}
    replacement = ''
    for ch in fixes:
        adj = fixes[ch]
        if adj < 0:
            replacement += ch*(-1*adj)
    perms = set(permutations(replacement))
    m = len(s)
    to_replace = ''
    for rep in perms:
        regex = '.*?'.join([ch for ch in rep])
        finds = re.findall(regex,s)
        if finds:
            x = sorted(finds, key=lambda x:len(x))[0]
            if m >= len(x):
                m = len(x)
                to_replace = x

    print_replacement(s, to_replace, fixes)

def print_replacement(inp, to_replace, fixes):
    replacement = ''
    for ch in to_replace:
        if fixes[ch] > 0:
            replacement += ch
    for ch in fixes:
        if fixes[ch] > 0:
            replacement += ch*fixes[ch]
    print(len(replacement))
    #print('{0}\t\t- Replace {1} with {2} (min length: {3})'.format(inp ,to_replace, replacement, len(replacement)))

def main():
    inputs =  ["GAAATAAA", "CACCGCTACCGC", "CAGCTAGC", "AAAAAAAA", "GAAAAAAA", "GATGAATAACCA", "ACGT"]
    for inp in inputs:
        find_min(inp)

if __name__ == '__main__':
    main()