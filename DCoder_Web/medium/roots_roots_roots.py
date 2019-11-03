import math
def findRoots( a, b, c):
# If a is 0, then equation is
# not quadratic, but linear
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        #print("Roots are real and different ")
        return ((-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a))
    elif d == 0:
        #print("Roots are real and same")
        return (-b / (2*a),-b / (2*a) )
    else: #d<0
        #print("Roots are complex")
        return (- b / (2*a) , " + i", sqrt_val)

a,b,c = [float(x) for x in input().split()]
print("{0:.2f}".format(sum(findRoots(a,b,c))))