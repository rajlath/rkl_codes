def arrayPreviousLess(a):
    r = []
    while a:
        v = a.pop()        
        h = -1
        for w in a:
            if w < v:
                h = w
        r = [h] + r
    return r

print(arrayPreviousLess([3, 5, 2, 4, 5])   )
