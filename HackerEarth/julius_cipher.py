from string import ascii_lowercase as lc
alphs = dict(zip(lc, range(1,27)))
for _ in range(input()):
    ins = raw_input().strip()
    if ins == ins[::-1]:
        print "Palindrome"
    else:
        vals = 1
        for x in ins:
            vals *= alphs[x]
        print vals