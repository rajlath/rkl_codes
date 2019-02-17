def slices(series, length):
    i = 0
    ret = []
    if length <1 or length > len(series):
        raise ValueError("Length is not proper")
    while i < len(series)-length+1:
        ret.append(series[i:i+length])
        i += 1
    return ret

#print(slices("7777", 0))




