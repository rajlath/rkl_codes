'''
8
! hello
! codeforces
? c
. o
? d
? h
. l
? e
'''

couldbe = set()
cantbe  = set()
commands = int(input())
disallowed = ""
es = 0
for i in range(commands):
    resp, words = [x for x in input().split()]
    tmp = set()
    for x in words:
        tmp.add(x)
    if resp =="!":
        for x in words:
            if 




