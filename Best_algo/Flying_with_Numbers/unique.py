'''
find all letters in word which is not repeated
'''
def keep_unique_letters(s):
    table = {}
    for i in s:
        table[i] = table.get(i, 0) + 1
    return "".join([x for x in table if table[x] == 1])


print(keep_unique_letters("google"))