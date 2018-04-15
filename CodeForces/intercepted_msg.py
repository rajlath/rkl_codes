'''
7 6
2 5 3 1 11 4 4
7 8 2 4 1 8
'''
def arr_sums(a):
    sum_arr = set()
    sums = 0
    for i in a:
        sums += i
        sum_arr.add(sums)
    return sum_arr

lena, lenb = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ass = arr_sums(a)
bs = arr_sums(b)
print(len(ass&bs))