#Check Permutation: Given two strings,
# write a method to decide if one is a permutation of the other.

# using sort
def is_permuatation_1(string1, string2):
    '''
    This method sorts both string and check char by char
    less efficient
    param : string1 : String
    param : string2 : String
    Return : Boolean: True if string1 permutation of string2 else False
    '''
    if len(string1) != len(string2):return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    for i, v in zip(sorted_string1 , sorted_string2):
        if i != v: return False
    return True

# by comparing char counts of both string
from collections import Counter
def is_permutation_2(string1, string2)    :
    '''
    This method sorts both string and check char by char
    less efficient
    param : string1 : String
    param : string2 : String
    Return : Boolean: True if string1 permutation of string2 else False
    '''
    count_string1 = Counter(string1)
    count_string2 = Counter(string2)
    for key, value in count_string1.items():
        if count_string2[key] != value:
            return False
    return True



print(is_permuatation_1("rajlath", "lathjar"))    #should return True
print(is_permuatation_1("rajlatha", "lathjars"))  #should return False
print(is_permutation_2("rajlath", "lathjar"))    #should return True
print(is_permutation_2("rajlatha", "lathjars"))  #should return Fals



