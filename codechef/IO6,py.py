from collections import Counter
def popular_words(text: str, words: list) -> dict:
    textc = [x.lower() for x in text.split()]
    textc= Counter(textc)

    ans  = {x:0 for x in words}
    for i in ans:
        ans[i] = textc.get(i, 0)

    return ans


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {'i': 4,'was': 3,'three': 0,'near': 0}
    print("Coding complete? Click 'Check' to earn cool rewards!")