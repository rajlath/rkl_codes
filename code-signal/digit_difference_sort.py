def digitDifferenceSort(a):
    def difference(s):
        sa = [ord(x) - 48 for x in str(s)]
        print(sa)
        rets =  max(sa) - min(sa)
        print(sa , rets)
        return rets
    ar = [(difference(x), i) for i, x in enumerate(a)]
    ar.sort(key=lambda k : (k[0], -k[1]))
    return [a[i] for _,i in ar]


a = [152, 23, 7, 887, 243]
print(digitDifferenceSort(a))
