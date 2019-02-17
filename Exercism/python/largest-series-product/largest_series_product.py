from functools import reduce
def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Size cannot be more then length of series.")
    if not series or size is 0:return 1
    series = [x for x in series]
    maxs = int(-10e12)
    for i in range(len(series) - size + 1):
        this = series[i:i+size]
        #print(this)
        maxs = max(maxs,reduce(lambda a, b: int(a) * int(b), this))
    return maxs

print(largest_product("0000", 2))


