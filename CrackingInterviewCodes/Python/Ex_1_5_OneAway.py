'''
One Away: There are three types of edits that can be performed on strings:
insert a character,remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''
'''
    params src String
    params tgt String
    return boolean
    return true if both the string can be made equal
    1. by replacing a letter in either src or tgt
    2. Adding a letter in either
    3. removing a letter in either
'''
# main function
def one_edit_away(str1, str2):
    if str1 == str2:return True
    lens, lent = len(str1), len(str2)
    if abs(lens - lent)  <= 1:
        if lens == lent:
            return one_edit_replacement(str1, str2)
        else:
            return one_edit_insert(str1, str2)
    else:
        return False

def one_edit_replacement(src, tgt):
    one_difference = False
    for x, y in zip(src, tgt):
        if x != y:
            if one_difference:return False
            one_difference = True
    return True

def one_edit_insert(src, tgt):
    srci = 0
    tgti = 0
    one_diff = False
    while srci < len(src) and tgti < len(tgt):
        if src[srci] != tgt[tgti]:
            if one_diff:
                return False
            if(len(src) > len(tgt)):srci+=1
            else:tgti+= 1
            one_diff = True
        else:
            tgti += 1
            srci += 1
    return True

print(one_edit_away("rajlath", "rajloth")) # return True a at index 4 should be replaced
print(one_edit_away("rajlath", "rajath"))  # 'l' to be added at index 3 return True
print(one_edit_away("rajlth", "rajlath"))  # 'a' to be added at index 4 return True
print(one_edit_away("rajlath", "rakloth")) # return False two mismatch







