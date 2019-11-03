import math
def is_prime(n):
    if n==1 or  n%2==0 and n != 2 or n%3==0 and n != 3 or n%5==0 and n != 5:return False
    for i in range(6,int(math.sqrt(n)), 5):
        if n % i == 0:return False
    return True

lens = int(input())
arrs = [int(x) for x in input().split()]
answ = 0
for i in arrs:
    answ += is_prime(i)
print(answ)