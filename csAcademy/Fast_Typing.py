from string import ascii_lowercase as lc
s = input()
c = [int(x) for x in input().split()]
dic = dict(zip(lc, c))
print(sum([dic[x] for x in s]))