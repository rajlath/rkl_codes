'''
def make_diamond(letter):
    mid = ord(letter) - ord("A")
    lens = mid * 2 + 1
    mid += 1
    left, rite = mid - 1, mid - 1
    begin = "A"
    ans = []
    while left > -1:
        curr = [" "] * lens
        curr[left] = begin
        curr[rite] = begin

        begin = chr(ord(begin) + 1)
        left -= 1
        rite += 1
        ans.append(''.join(curr))
    for i in range(mid - 2, -1, -1):
        ans.append(ans[i])
    return "\n".join(ans)

'''
from string import ascii_uppercase as au

def make_diamond(letter):
    lines = []
    length = au.index(letter) + 1
    for l in range(length):
        line = [' '] * length
        line[l] = au[l]
        lines.append(''.join(list(reversed(line)) + line[1:]))
    return '\n'.join(lines[:-1] + list(reversed(lines))) + '\n'



print(make_diamond("E"))