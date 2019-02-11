'''
a methohd which compresses a string by replacing repeated chars with
count of repeating chars and char.
In case chars is not repeated, count is not prefixed.
if length of the compressed is not smaller then original string return original
'''
def compress_string(s):
    compressed = ''
    last = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            if count == 1:
                compressed += last
                last = s[i]
            else:
                compressed += str(count) + last
                last = s[i]
                count= 1
    return compressed + str(count) + last




original = "aa"
compress = compress_string(original)
print([compress, original][len(original)<=len(compress)])








