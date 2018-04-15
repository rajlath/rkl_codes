def checkValidity(a, b, c):

    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True


iso = 0
for i in range(int(input())):
    a, b , c = [int(x) for x in input().split()]
    if checkValidity(a, b, c):
        if a == b == c:
            print("equilateral")
        elif len(set([a, b, c])) == 3:
            print("scalene")
        else:
            iso+=1
            print("isosceles")
    else:
        print("not triangle")
print(iso)