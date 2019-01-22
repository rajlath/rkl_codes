from string import ascii_lowercase as lc
ins = input()
more = int(input())
values = [int(x) for x in input().split()]
val_dic = dict(zip(lc, values))
max_is = ins + lc[values.index(max(values))] * more
print(sum([val_dic[x] * (i + 1) for i, x in enumerate(max_is)]))
