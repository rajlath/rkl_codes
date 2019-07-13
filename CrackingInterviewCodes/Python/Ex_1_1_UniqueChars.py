#Is Unique:
#Implement an algorithm to determine if a string has all unique characters.

def is_unique_chars_1(str):
    '''
    method 1 : using hash table
    param str : string - string to check  for unique chars
    return boolean : True if has all unique char else False
    '''
    chars = [0] * 128
    for x in str:
        i = ord(x)
        if chars[i]:
            return False
        chars[i] = 1
    return True


from collections import defaultdict
def is_unique_chars_2(str):
    '''
    method 2 : using dictionary
    param str : string - string to check  for unique chars
    return boolean : True if has all unique char else False
    '''
    chars = defaultdict(int)
    for i in str:
        if chars[i] != 0:
            return False
        chars[i] = 1
    return True

def is_unique_chars_3(str):
    '''
    method 3 : using bit vector
    param str : string - string to check  for unique chars
    return boolean : True if has all unique char else False
    '''
    checker = 0
    for i in str:
        value = ord(i)
        if checker & (1 << value) > 0:
            return False
        checker |= (1 << value)
    return True





print(is_unique_chars_1("rajkumar")) # False a is repeated
print(is_unique_chars_1("rajkumsl")) # All Chars are unique

print(is_unique_chars_2("rajkumar")) # False a is repeated
print(is_unique_chars_2("rajkumsl")) # All Chars are unique

print(is_unique_chars_3("rajkumar")) # False a is repeated
print(is_unique_chars_3("rajkumsl")) # All Chars are unique



