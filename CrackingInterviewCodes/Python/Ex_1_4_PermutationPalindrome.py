'''
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atco eta·; etc.)
'''
'''
    param str String
    return Boolean
    case insensetive check is used.
    spaces are ignored.
'''

def is_permuatation_palindrome(str):
    counts = dict()
    for i in str:
        if i.isalpha():
            i = i.lower()
            if i in counts:
                counts[i] ^= 1
            else:
                counts[i] = counts.get(i, 1)
    #print(counts)
    if sum(counts.values()) > 1:
        return False
    return True

print(is_permuatation_palindrome( "atco ctaaa"))


