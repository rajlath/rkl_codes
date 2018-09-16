str1 = "marina"
str2 = "anaram"

def verify_anagrams(s1, s2):
    '''
    verify if two strings are anagram to each other
    '''
    dicts = {}
    if len(s1) != len(s2):return False
    for i in range(len(s1)):
        dicts[s1[i]] = dicts.get(s1[i], 0) + 1
        dicts[s2[i]] = dicts.get(s2[i], 0) - 1
    return all([ x == 0 for x in dicts.values()])



def verify_anagrams_1(s1, s2):
    if len(s1) != len(s2): return False
    sum1 = sum([ord(x) for x in str1]) % 11
    sum2 = sum([ord(x) for x in str2]) % 11
    return sum1 == sum2

print(verify_anagrams(str1, str2))
print(verify_anagrams_1(str1, str2))





