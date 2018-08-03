def compress_string(s):
    '''
    compress a string by substituting repeated char with count
    mention count only if greater then 1
    replace with compress only if compressed length is less then
    uncompressed length
    ins : string
    out : string
    '''

    last = ''
    cnts = 0
    ucstr=''
    for ch in s:
        if ch == last:cnts += 1
        else:
            ucstr += last
            if cnts > 1:
                ucstr += str(cnts)
            cnts = 1
            last = ch
    ucstr += last
    if cnts > 1:ucstr += str(cnts)
    return ucstr


print(compress_string("a"))


