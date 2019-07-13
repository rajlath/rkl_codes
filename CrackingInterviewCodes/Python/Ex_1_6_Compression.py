'''
1.6 String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z)
'''

'''
    param str String: String which is to be compressed
    return String if compressed string is larger then original return original
'''
# uses normal method having a pointer to count repeatation
def string_compression_1(strs):
    consecutive_count = 0
    compressed = ''
    for i,v in enumerate(strs):
        consecutive_count += 1
        further = i + 1
        if further >= len(strs) or strs[further] != strs[i]:
            compressed += (v + str(consecutive_count))
            consecutive_count = 0
    if len(compressed) > len(strs):compressed = strs
    return compressed


# uses groupby to gather consecutive chars
from itertools import groupby
def string_compression_2(strs):
    scg = groupby(strs)
    compressed = ''
    for i in scg:
        compressed += i[0] + str(len(list(i[1])))
    if len(compressed) > len(strs):compressed = strs
    return compressed


print(string_compression_1("aabcccaabbcc"))
print(string_compression_2("aabcccaabbcc"))





