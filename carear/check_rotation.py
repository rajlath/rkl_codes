def is_string_rotated(s, t):
    '''
    check whether t is an rotation of s
    by rotation we mean that every chars
    in source is clockwise shifted to a constanct place
    in t
    ins : s string and t string
    ret : boolean

    '''
    st = s + t
    if t in st and len(t) == len(s) and len(s)!=0 and len(t)!=0:return True
    else:return False



print(is_string_rotated("", ""))

