#Friend in Need
#https://www.codechef.com/NACA2019/problems/FNEE

def is_prime(n):
    if n <= 1:return False
    for i in range(2, n - 1):
        if n % i == 0:return False
    return True

nb_test = int(input())
for _ in range(nb_test):
    curr = int(input())
    def answer(curr1):
        while curr1 > 1:
            if is_prime(curr1): return str(curr1)
            curr1 -= 1
    if   curr == 1:print("1 1")
    elif curr == 2:print("2 1")
    else: print(answer(curr), 1)


