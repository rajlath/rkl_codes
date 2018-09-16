'''
5
101 5
000 3
001 5
010 1
111 9
4
00
1
0
011
'''
mod = 1000000007
nos = int(input())
dicts = {}
for i in range(nos):
    a, b = [x for x in input().split()]
    dicts[a] = b
for i in range(int(input()))    :
    curr = input()
    sums = 0
    for i,v in dicts.items():
        if i.startswith(curr):sums += int(v)
    print(sums%mod)
