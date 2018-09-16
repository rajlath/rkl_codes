from itertools import groupby
def lineEncoding(s):
    ret = ''
    for k, g in groupby(s):
        lens = str(len(list(g)))
        ret += lens + k if int(lens)>1 else k
    print(ret)




lineEncoding("aaabbbbccd")