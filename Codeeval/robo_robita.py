#58.52

import sys
testcases = open(sys.argv[1],'r')
for test in testcases:
    i, j = test.split("|")
    a, b = map(int, i.split("x"))
    x, y = map(int, j.split())
    r = 0
    while b != y:
        r, a, b, x, y = r+a, b-1, a, b-y, x
        
    print r + x
