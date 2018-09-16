for _ in range(int(input())):
    a, b = [x for x in input().split()]
    try:
        print( int(a) // int(b))
    except ValueError as ex:
        print("Error Code: {}".format(ex))

    except ZeroDivisionError as ex:
        print("Error Code: {}".format(ex))


import re
for _ in range(int(input())):
    r = input()
    try:
        re.compile(r)
        print(True)
    except re.error:
        print(False)



