def is_anagram(s, t):
    '''
    check whether t is an anagram/permuation of s
    ins s a string   t a string
    return boolean

    iterate through both the array
    increment char count in first array
    decrement char count in second arr
    if count is less then 0:its fasle
    '''
    chars = {}
    for i in s:chars[i] = chars.get(i, 0) +1
    for j in t:
        chars[j]-= 1
        if not chars[j] or chars[j]<0:return False
    return True


print(is_anagram("raj", "jar"))

