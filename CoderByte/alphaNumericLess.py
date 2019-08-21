import re

def alphanumericLess(s1, s2):
    seq1 = ([i for i in re.split(r'(\d+|\D)', s1) if i])
    seq2 = ([i for i in re.split(r'(\d+|\D)', s2) if i])
    print(seq1, seq2)
    for x, y in zip(seq1, seq2):
        if x != y:
            if x.isdigit() and y.isdigit():
                if int(x) != int(y):
                    return False
            else:
                return False

    return True

print(alphanumericLess("x11y012", "x011y13"))
