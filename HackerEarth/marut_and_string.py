
def check_invalid_test(a):
    try:
        a = int(a)
    except ValueError:
        return False
    if a not in range(1, 11):
        return False
    return True


N = input()
if not check_invalid_test(N):
    print("Invalid Test")
else:
    N = int(N)
    for _ in range(N):
        ins = input()
        lens= len(ins)
        if lens not in range(1, 101):
            print("Invalid Input")
            continue
        else:
            lcl = sum([1 for c in ins if c.islower()])
            ucl = sum([1 for c in ins if c.isupper()])
            if  lcl+ucl == 0:
                print ("Invalid Input")
                continue
            else:
                print(min(lcl,ucl))


