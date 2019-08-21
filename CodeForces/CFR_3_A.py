a, ai = [x for x  in input()]
b, bi = [x for x  in input()]
ai, bi = int(ai), int(bi)
path = []
while a != b or ai != bi:
    curr = ''
    if a < b :
        curr += 'R'
        a = chr(ord(a) + 1)
    if a > b :
        curr += 'L'
        a = chr(ord(a) - 1)
    if ai > bi:
        curr +=  "D"
        ai -= 1
    if ai < bi:
        curr += "U"
        ai += 1
    
    path.append(curr)
print(len(path))
print("\n".join(path))
