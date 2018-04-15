import math
def is_square(n):

    if int(n**0.5)**2 == int(n):
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    for i in range(1, int(n**0.5)+1):
        if is_square(n - (i*i)):
            a = int(math.sqrt(n-i*i))
            print(max(i, a), min(i, a))
            break






