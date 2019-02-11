def helper(s, begin, end):
    while begin <= end and begin >= 0 and end < len(s) and s[begin] == s[end]:
        begin -= 1
        end   += 1
    return s[begin+1:end]

def longest_palindrome_in_String(s):
    if s is None or len(s) == 1:return s
    lens   = len(s)
    longest = s[0]
    for i in range(lens):
        curr = helper(s,i, i)
        if len(curr) > len(longest):
            longest = curr
        curr = helper(s, i, i+1)
        if len(curr) > len(longest):
            longest = curr
    return longest


print(longest_palindrome_in_String("dabcba"))

