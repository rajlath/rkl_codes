def longestDigitsPrefix(inputString):
    ans = ''
    for i in inputString:
        if i not in "0123456789":
            break
        else:
            ans += i
    return ans


print(longestDigitsPrefix("  3) always check for whitespaces"))