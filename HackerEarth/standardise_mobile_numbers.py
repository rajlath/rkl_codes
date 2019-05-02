def wrapper(f):
    def fun(l):
        for ll in l:
            lens = len(ll)
            if lens == 10: ll = "+91 {} {}".format(ll[:5],ll[5:])
            elif lens == 11: ll = "+91 {} {}".format(ll[1:6],ll[6:])
            elif lens == 12: ll = "+91 {} {}".format(ll[2:7],ll[7:])
        return l
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)