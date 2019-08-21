import re
def reverseInParentheses(inputString):
    reg_pat = re.compile(r"(\([^()]*\))")
    while re.search(reg_pat, inputString):
        has = re.findall(reg_pat, inputString)
        for i in has:
            inputString = inputString.replace(i, i[1:-1][::-1])
    return inputString


print(reverseInParentheses("foo(bar(baz))blim"))
