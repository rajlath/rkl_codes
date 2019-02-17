def append(xs, ys):
    return concat([xs, ys])


def concat(lists):
    return [x for lst in lists for x in lst]


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def length(xs):
    return sum([1 for x in xs])


def map_clone(function, xs):
    return [function(x) for x in xs]


def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc


def foldr(function, xs, acc):
    return foldl(lambda x, acc: function(acc, x), reverse(xs), acc)



def reverse(xs):
    return foldl(lambda acc, x: append([x], acc), xs, [])

#print(append([1,2, 3], [4, 5, 6]))
#print(length([1, 2, 3, 4]))
