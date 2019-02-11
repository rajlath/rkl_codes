'''
An efficient algo to check whether a string consist of unique chars only
'''
def is_all_unique_in_string(s):
    checker = {}
    for i in s:
        if i in checker:return False
        checker[i] = checker.get(i, 0) + 1
    return True

def is_all_unique_in_string_2(s):
    checker = 0
    for i in range(len(s)):
        val = ord(s[i]) - ord('a')
        off = 1 << val
        #print(checker)
        if ((checker & off) > 0):return False
        checker |= off
        #print(checker)
    return True


print(is_all_unique_in_string_2("abcdefdgh"))
