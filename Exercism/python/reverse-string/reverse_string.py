def reverse(text):
    ans = ''
    if len(text) == 1:return text
    text = list(text)
    while text:
        ans += text.pop()
    return ans
