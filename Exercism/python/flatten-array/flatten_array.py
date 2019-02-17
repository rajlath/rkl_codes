import itertools
def flatten(iterable):
    if type(iterable) is str:return list(iterable)
    flat = []
    for i in iterable:
        try:
            flat.extend(flatten(i))
        except TypeError:
            if i is not None:
                flat.append(i)
    return flat

#print(flatten([1,[2,3,None,4],[None],5]))
