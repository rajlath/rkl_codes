from string import ascii_lowercase as lc
def stolenLunch(note):
    rets = ''
    for x in note:
        rets += [x, lc[int(x)]][x.isdigit()==True]
    return rets

print(stolenLunch())

