def is_unique_char_1(s):
    '''
    check wether an array s contains only unique chars
    ins : String, array of chars
    out : Boolean
    '''
    if len(s)>256:
        return False
    all_chars = [0]* 256
    for i in range(len(s)):
        if all_chars[ord(s[i])]:return False
        all_chars[ord(s[i])] = 1
    return True

def is_unique_char_2(s):
    '''
    check wether an array s contains only unique chars
    uses bit manipulation
    s consist of lower case letters.
    ins : String, array of chars
    out : Boolean
    '''
    checker= int(0)
    for i in range(len(s)):
        val = ord(s[i])
        if checker  &  (1 << val) > 0: return False
        checker |=  (1 << val)
    return True

print(is_unique_char_2("abcdefa"))




